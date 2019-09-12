import logging
import sys
from typing import List

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


class FSMMachine(FSMState):
    states: List[FSMState] = []
    state: FSMState = None
    default_state: FSMState = None

    # screen用来更新画面,ai_controller控制画面, state用来告诉ai_controller该用什么状态
    def __init__(self, screen, ai_controller):
        super().__init__(screen, ai_controller)
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

        # 设置默认状态
        self.current_state = idle_state

    # 获取当前状态
    def get_current_state(self):
        return self.current_state

    # 添加状态
    def add_state(self, state: FSMState):
        self.states.append(state)

    # 销毁对象
    def destroy(self):
        self.states.clear()

    def trans_state(self, goal_state: FSMStateEnum):
        for state in self.states:
            if state.type() == goal_state:
                # 退出老的状态
                self.current_state.exit()
                self.current_state = state
                # 进入新的状态
                self.current_state.enter()

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
    def update(self):
        for e in event.get():
            # 退出游戏检测
            if e.type == GameEvent.quit:
                self.exit_game()
            # 以下为UI状态转换
            if e.type == GameEvent.start_game:
                self.trans_state(FSMStateEnum.Playing)
            if e.type == GameEvent.pause_game:
                self.trans_state(FSMStateEnum.Pause)
            if e.type == GameEvent.end:
                self.trans_state(FSMStateEnum.End)
            if e.type == GameEvent.idle:
                self.trans_state(FSMStateEnum.Idle)
            # 以下为玩家按键操作检测
            if e.type == GameEvent.move_left:
                if self.current_state == FSMStateEnum.Playing:
                    self.move_left()
            if e.type == GameEvent.move_right:
                if self.current_state == FSMStateEnum.Playing:
                    self.move_right()

            self.current_state.update_view()
