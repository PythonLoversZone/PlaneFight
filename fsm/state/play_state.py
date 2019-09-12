from fsm.fsm import FSM, FsmState


# 运行状态
class PlayingState(FSM):

    def __init__(self, screen, ai_controller, state=FsmState.Playing):
        super().__init__(screen, ai_controller, state)
