import logging

from fsm.fsm_state import FSMStateEnum, FSMState

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


# 暂停状态
class PauseState(FSMState):

    def __init__(self, screen, ai_controller):
        super().__init__(screen, ai_controller)

    def enter(self):
        logger.info('进入pause状态...')
        super().enter()

    def exit(self):
        logger.info('退出pause状态...')
        super().exit()

    def update_view(self):
        logger.info('更新pause状态...')
        super().update_view()

    def type(self):
        return FSMStateEnum.Pause
