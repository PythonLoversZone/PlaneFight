import logging

import pygame

from config.game_config import Resource
from fsm.fsm_state import FSMStateEnum, FSMState
from model.obj.player import Player

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


# 运行状态
class PlayingState(FSMState):
    player_group = None

    def __init__(self, screen, ai_controller):
        super().__init__(screen, ai_controller)

    def type(self):
        return FSMStateEnum.Playing

    def enter(self):
        logger.info('进入play状态...')
        super().enter()
        player = Player(Resource.player, 0)
        self.player_group = pygame.sprite.Group(player)

    def exit(self):
        logger.info('退出play状态...')
        super().exit()

    def update_view(self):
        logger.info('更新play状态...')
        super().update_view()
        self.player_group.update()
        self.player_group.draw(self.screen)
