import pygame
from pygame.sprite import Sprite

"""游戏基类"""


class GameObject(Sprite):

    def __init__(self, image, speed=1):
        super().__init__()

        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        super().update()
        self.rect.y += self.speed
