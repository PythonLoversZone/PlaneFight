"""显示分数的label"""
import pygame

from config.game_config import Colors, GameConfig


class Label(object):
    def __init__(self, label='', position=None, color=Colors.black):
        my_font = pygame.font.SysFont('Comic Sans MS', 30)
        self.label = my_font.render(label, False, color)
        if position is None:
            self.x = GameConfig.screen.width / 2
            self.y = GameConfig.screen.height / 2
