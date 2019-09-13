import logging

from fsm.fsm_state import FSMStateEnum, FSMState

# 初始状态 仅一个背景和一个开始按钮
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class IdleState(FSMState):

    def __init__(self, screen, ai_controller):
        super().__init__(screen, ai_controller)

    def enter(self):
        logger.info('进入idle状态...')
        super().enter()

    def exit(self):
        logger.info('退出idle状态...')
        super().exit()

    def type(self):
        return FSMStateEnum.Idle

    def update_view(self):
        logger.info('更新idle视图......')
        super().update_view()
        self.back_group.draw(self.screen)
        self.back_group.update()
