import logging

from fsm.fsm_state import FSMStateEnum, FSMState

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

    def exit(self):
        logger.info('退出play状态...')
        super().exit()

    def update_view(self):
        logger.info('更新play状态...')
        super().update_view()
