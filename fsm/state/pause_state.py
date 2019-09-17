import logging

from fsm.fsm_state import FSMStateEnum
from fsm.state.play_state import PlayingState

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


# 暂停状态
class PauseState(PlayingState):

    def __init__(self, screen, ai_controller):
        super().__init__(screen, ai_controller)

    def enter(self):
        logger.info('进入pause状态...')

    def exit(self):
        logger.info('退出pause状态...')

    def update_view(self):
        pass

    def type(self):
        return FSMStateEnum.Pause
