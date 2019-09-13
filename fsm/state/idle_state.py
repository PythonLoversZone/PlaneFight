import logging

import pygame

from config.game_config import Resource
from config.game_util import GameUtil
from fsm.fsm_state import FSMStateEnum, FSMState
# 初始状态 仅一个背景和一个开始按钮
from model.ui.button import Button

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class IdleState(FSMState):

    def __init__(self, screen, ai_controller):
        super().__init__(screen, ai_controller)

    def enter(self):
        logger.info('进入idle状态...')
        super().enter()
        # 画一个按钮
        surface_image = Resource.create_image(Resource.start_game)
        position = GameUtil.get_center_position(surface_image)
        self.start_button = Button(surface_image, position)

    def exit(self):
        logger.info('退出idle状态...')
        super().exit()

    def type(self):
        return FSMStateEnum.Idle

    def update_view(self):
        super().update_view()
        # 放到正中间
        position = (self.start_button.rect.x, self.start_button.rect.y)
        self.screen.blit(self.start_button.image, position)
        # 刷新
        pygame.display.flip()
