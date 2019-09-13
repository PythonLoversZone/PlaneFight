import logging
import sys
from typing import Dict

import pygame
from pygame import event

from fsm.fsm_state import FSMStateEnum, FSMState
from fsm.state.end_state import EndState
from fsm.state.idle_state import IdleState
from fsm.state.pause_state import PauseState
from fsm.state.play_state import PlayingState
from game_event.game_event import GameEvent

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class FSMMachine:
    states: Dict[FSMStateEnum, FSMState] = {}
    state: FSMState = None

    # screen用来更新画面,ai_controller控制画面, state用来告诉ai_controller该用什么状态
    def __init__(self, screen, ai_controller):
        logger.info('初始化状态机....')
        self.screen = screen
        self.controller = ai_controller
        # 添加状态
        idle_state = IdleState(screen, ai_controller)
        self.add_state(idle_state)
        playing_state = PlayingState(screen, ai_controller)
        self.add_state(playing_state)
        pause_state = PauseState(screen, ai_controller)
        self.add_state(pause_state)
        end_state = EndState(screen, ai_controller)
        self.add_state(end_state)

        # 初始化状态
        logger.info('设置默认状态为idle....')
        self.set_state(FSMStateEnum.Idle)

    # 获取当前状态
    def get_state(self):
        return self.state

    # 获取当前状态
    def set_state(self, state: FSMStateEnum):
        # 退出老的状态
        if self.state is not None:
            self.state.exit()
        # 设置新的状态
        self.state = self.states[state]
        # 进入新的状态
        self.state.enter()

    # 添加状态
    def add_state(self, state: FSMState):
        key = state.type()
        self.states[key] = state

    # 销毁对象
    def destroy(self):
        self.states.clear()
        logger.info('destroy....')

    # 检测状态变化
    def check_trans_state(self):
        pass

    # 状态转换
    def trans_state(self, goal_state: FSMStateEnum):
        # 如果在状态列表中找到了目标状态,并且当前状态不是目标状态则进入该状态
        if self.states.__contains__(goal_state):
            if self.state is None:
                self.set_state(goal_state)
                return
            # 状态相同就不需要切换
            if self.state.type() == goal_state:
                return
            self.set_state(goal_state)

    # 退出游戏
    @staticmethod
    def exit_game():
        pygame.quit()
        sys.exit()

    # 事件处理
    @staticmethod
    def move_left():
        logger.info('pressed d ')

    @staticmethod
    def move_right():
        logger.info('pressed a ')

    # 每秒60(fps)次监听玩家的动作,不同的动作转入不同的状态中去,具体的逻辑在各自的状态中处理
    def update_machine(self):
        # 不停的检测状态是否有变化
        self.check_trans_state()
        # 更新UI
        self.state.update_view()

        for e in event.get():
            # 退出游戏检测
            if e.type == GameEvent.quit:
                self.exit_game()
                logger.info('关闭游戏.........')
            # 以下为玩家按键操作检测
            if e.type == GameEvent.move_left:
                if self.state.type() == FSMStateEnum.Playing:
                    self.move_left()
                    logger.info('左移.........')
            if e.type == GameEvent.move_right:
                if self.state.type() == FSMStateEnum.Playing:
                    self.move_right()
                    logger.info('右移.........')
