from pygame.sprite import Sprite

"""游戏基类"""


class GameObject(Sprite):

    def __init__(self, image):
        super().__init__()
