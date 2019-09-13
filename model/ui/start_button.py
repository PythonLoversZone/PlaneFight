from config.game_config import Resource, GameConfig
from model.game_object import GameObject

"""开始按钮"""


class StartButton(GameObject):
    def __init__(self):
        # 创建按钮
        super().__init__(Resource.start_game, 0)
        # 设置按钮的位置
        self.rect.x = (GameConfig.screen.width - self.rect.width) / 2
        self.rect.y = (GameConfig.screen.height - self.rect.height) / 2

    def update(self):
        super().update()
