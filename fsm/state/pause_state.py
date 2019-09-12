from fsm.fsm_state import FSMStateEnum, FSMState


# 暂停状态
class PauseState(FSMState):

    def __init__(self, screen, ai_controller):
        super().__init__(screen, ai_controller)

    def type(self):
        return FSMStateEnum.Pause
