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
    screen: Surface = None

    controller: AIController = None

    def __init__(self, screen, ai_controller) -> None:
        self.screen = screen
        self.controller = ai_controller

    def type(self):
        pass

    # 销毁对象
    def destroy(self):
        pass

    # 更新界面
    def update_view(self):
        pass

    # ------------------------------以下方法需要子类实现------------------------------------
    # 退出当前状态
    def exit(self):
        pass

    # 进入当前状态,创建背景
    def enter(self):
        pass
# ------------------------------以上方法需要子类实现------------------------------------
