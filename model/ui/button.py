from enum import Enum

import pygame
from pygame.surface import Surface


class ClickType(Enum):
    left_click = 1
    mid_click = 2
    right_click = 3


# 按钮
class Button(object):

    # 需要一个load的image和它应该放的位置
    def __init__(self, image: Surface, position):
        # 创建按钮
        self.image = image
        self.rect = pygame.Rect(position, (image.get_width(), image.get_height()))

    # 默认为左单击,1为左单击,2为右单击
    def click(self, event, click_type=ClickType.left_click):
        if event.type == pygame.MOUSEBUTTONDOWN:  # is some button clicked
            x, y = event.pos
            if event.button == click_type.value:  # is left button clicked
                if self.rect.collidepoint(x, y):  # is mouse over button
                    return True
                return False
