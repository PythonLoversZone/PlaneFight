from fsm.fsm_state import FSMStateEnum, FSMState


# 运行状态
class PlayingState(FSMState):

    def __init__(self, screen, ai_controller, state=FSMStateEnum.Playing):
        super().__init__(screen, ai_controller, state)
