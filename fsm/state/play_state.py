import logging

import pygame

from config.game_config import Resource, GameConfig
from fsm.fsm_state import FSMStateEnum, FSMState
from model.obj.enemy import Enemy
from model.obj.player import Player
from model.ui.button import Button
from model.ui.label import Label

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


# 运行状态
class PlayingState(FSMState):

    def __init__(self, screen, ai_controller):
        super().__init__(screen, ai_controller)

    def type(self):
        return FSMStateEnum.Playing

    def enter(self):
        logger.info('进入play状态...')
        super().enter()
        # 玩家
        self.player = Player(Resource.player, 0)

        # 暂停按钮
        self.pause_button = Button(Resource.pause)
        self.pause_button.rect.x = GameConfig.screen.width - 100
        self.pause_button.rect.y = 80

        # 分数
        my_font = pygame.font.SysFont('Comic Sans MS', 30)
        self.score = Label('0')
        self.score.x = GameConfig.screen.width - 80
        self.score.y = 10

    def exit(self):
        logger.info('退出play状态...')
        super().exit()

    def update_view(self):
        super().update_view()
        # 玩家
        self.player.update()
        self.screen.blit(self.player.image, self.player.rect)
        # 暂停按钮
        self.pause_button.update()
        self.screen.blit(self.pause_button.image, self.pause_button.rect)
        # 分数
        self.screen.blit(self.score.label, (self.score.x, self.score.y))

        # 敌人
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

    def enemy_enter(self):
        enemy = Enemy()
        self.enemy_group.add(enemy)
