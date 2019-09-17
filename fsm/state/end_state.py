import logging

from config.game_config import Resource
from fsm.fsm_state import FSMStateEnum, FSMState
from model.ui.button import Button

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


# 游戏结束状态 显示当前分数和重新开始按钮
class EndState(FSMState):

    def __init__(self, screen, ai_controller):
        super().__init__(screen, ai_controller)

    def enter(self):
        logger.info('进入end状态...')
        super().enter()
        self.restart_button = Button(Resource.restart_game)

    def exit(self):
        logger.info('退出end状态...')
        super().exit()

    def update_view(self):
        super().update_view()
        self.restart_button.update()
        self.screen.blit(self.restart_button.image, self.restart_button.rect)

    def type(self):
        return FSMStateEnum.End
