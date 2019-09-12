from enum import Enum

from fsm.state.end_state import EndState
from fsm.state.idle_state import IdleState
from fsm.state.pause_state import PauseState
from fsm.state.play_state import PlayingState

"""状态机"""


class FsmState(Enum):
    Idle = 1
    Playing = 2
    Pause = 3
    End = 4


class FSM:
    states = []

    current_state = None

    # screen用来更新画面,ai_controller控制画面, state用来告诉ai_controller该用什么状态
    def __init__(self, screen, ai_controller, state=FsmState.Idle):
        # 添加状态
        self.add_state(IdleState(screen, ai_controller))
        self.add_state(PlayingState(screen, ai_controller))
        self.add_state(PauseState(screen, ai_controller))
        self.add_state(EndState(screen, ai_controller))

        # 设置默认状态
        self.set_default_state(state)

    # 进入当前状态
    def enter(self):
        pass

    # 退出当前状态
    def exit(self):
        pass

    # 销毁对象
    def destroy(self):
        pass

    # 检查转换
    def check_transitions(self):
        pass

    # 更新界面
    def update(self):
        pass

    # 添加状态
    def add_state(self, state):
        self.states.append(state)
        pass

    # 状态转换
    def trans_state(self, state):
        pass

    # 获取当前状态
    def get_current_state(self):
        return self.current_state

    # 设置默认状态
    @staticmethod
    def set_default_state(state):
        current_state = state
