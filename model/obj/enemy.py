import logging
import random

from config.game_config import Resource, GameConfig
from model.game_object import GameObject

"""敌军"""

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class Enemy(GameObject):

    def __init__(self, speed=1):
        super().__init__(Resource.enemy1, GameConfig.enemy_move_speed)
        self.rect.x = random.randint(self.rect.width, GameConfig.screen.width - self.rect.width)
        self.rect.y = -self.rect.height

    def update(self):
        super().update()
        if self.rect.y >= GameConfig.screen.height:
            self.kill()

    def __del__(self):
        logger.info('-----------敌人销毁------------')
