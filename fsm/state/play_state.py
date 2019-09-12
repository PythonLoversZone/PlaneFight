from fsm.fsm_state import FSMStateEnum, FSMState


# 运行状态
class PlayingState(FSMState):

    def __init__(self, screen, ai_controller):
        super().__init__(screen, ai_controller)

    def type(self):
        return FSMStateEnum.Playing
