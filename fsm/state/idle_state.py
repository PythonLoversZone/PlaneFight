import logging

import pygame

from fsm.fsm_state import FSMStateEnum, FSMState
# 初始状态 仅一个背景和一个开始按钮
from model.ui.start_button import StartButton

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class IdleState(FSMState):
    # 按钮精灵组
    button_group = None

    def __init__(self, screen, ai_controller):
        super().__init__(screen, ai_controller)

    def enter(self):
        logger.info('进入idle状态...')
        super().enter()
        start_button = StartButton()
        self.button_group = pygame.sprite.Group(start_button)
        # 在最中间画一个按钮

    def exit(self):
        logger.info('退出idle状态...')
        super().exit()

    def type(self):
        return FSMStateEnum.Idle

    def update_view(self):
        logger.info('更新idle视图......')
        super().update_view()
        self.button_group.update()
        self.button_group.draw(self.screen)
