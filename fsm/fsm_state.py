from enum import Enum

from pygame.surface import Surface

from fsm.ai_controller import AIController
# 状态枚举
from model.ui.background import Background


class FSMStateEnum(Enum):
    Idle = 1
    Playing = 2
    Pause = 3
    End = 4


class FSMState:
    # 当前状态
    state: FSMStateEnum = None

    # 默认状态
    default_state: FSMStateEnum = None

    screen: Surface = None

    controller: AIController = None

    def __init__(self, screen, ai_controller, state) -> None:
        self.state = state
        self.screen = screen
        self.controller = ai_controller

    # 销毁对象
    def destroy(self):
        pass

    # 更新界面
    def update(self):
        pass

    # 添加状态
    def add_state(self, state):
        pass

    # 获取当前状态
    def get_current_state(self):
        return self.state

    # ------------------------------以下方法需要子类实现------------------------------------
    # 退出当前状态
    def exit(self):
        pass

    # 检查转换
    def check_transitions(self):
        pass

    # 状态转换
    def trans_state(self, goal_state):
        pass

    # 进入当前状态,创建背景
    def enter(self):
        Background()
# ------------------------------以上方法需要子类实现------------------------------------
