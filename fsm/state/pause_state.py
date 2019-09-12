from fsm.fsm_machine import FSMMachine

from fsm.fsm_state import FSMStateEnum


# 暂停状态
class PauseState(FSMMachine):

    def __init__(self, screen, ai_controller, state=FSMStateEnum.Pause):
        super().__init__(screen, ai_controller, state)
