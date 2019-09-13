from config.game_config import GameConfig
from model.game_object import GameObject

"""玩家"""


class Player(GameObject):
    def __init__(self, image, speed):
        super().__init__(image, speed)
        self.rect.x = (GameConfig.screen.width - self.rect.width) / 2
        self.rect.y = GameConfig.screen.height-self.rect.height-20

    def update(self):
        super().update()
