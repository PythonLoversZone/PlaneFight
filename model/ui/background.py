from config.game_config import GameConfig, Resource
from model.game_object import GameObject


# 背景
class Background(GameObject):
    def __init__(self, is_repeat=False):
        super().__init__(Resource.background)
        if is_repeat:
            self.rect.y = self.rect.height

    def update(self):
        super().update()
