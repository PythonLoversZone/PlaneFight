from fsm.fsm import FSM, FsmState


# 暂停状态
class PauseState(FSM):

    def __init__(self, screen, ai_controller, state=FsmState.Pause):
        super().__init__(screen, ai_controller, state)
