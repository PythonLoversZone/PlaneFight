from enum import Enum

import pygame
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

    # 背景精灵组
    back_group = None

    def __init__(self, screen, ai_controller) -> None:
        self.screen = screen
        self.controller = ai_controller

    # 进入当前状态,创建背景
    def enter(self):
        bg1 = Background()
        bg2 = Background(True)
        self.back_group = pygame.sprite.Group(bg1, bg2)

    # ------------------------------以下方法需要子类实现------------------------------------
    # 退出当前状态
    def exit(self):
        pass

    def type(self):
        pass

    # 销毁对象
    def destroy(self):
        pass

    # 更新
    def update_view(self):
        # 更新背景组精灵
        self.back_group.update()
        self.back_group.draw(self.screen)
# ------------------------------以上方法需要子类实现------------------------------------
