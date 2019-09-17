from enum import Enum

import pygame
from pygame.surface import Surface

from config.game_config import GameConfig
from model.game_object import GameObject


class ClickType(Enum):
    left_click = 1
    mid_click = 2
    right_click = 3


# 按钮
class Button(GameObject):

    # 需要一个load的image和它应该放的位置
    def __init__(self, image, position=None):
        # 创建按钮
        super().__init__(image, 0)
        # 位置
        if position is None:
            self.rect.x = (GameConfig.screen.width - self.rect.width) / 2
            self.rect.y = (GameConfig.screen.height - self.rect.height) / 2

    # 默认为左单击,1为左单击,2为右单击
    def click(self, event, click_type=ClickType.left_click):
        if event.type == pygame.MOUSEBUTTONDOWN:  # is some button clicked
            x, y = event.pos
            if event.button == click_type.value:  # is left button clicked
                if self.rect.collidepoint(x, y):  # is mouse over button
                    return True
                return False
