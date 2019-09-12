from fsm.fsm import FSM, FsmState


# 初始状态 仅一个背景和一个开始按钮
class IdleState(FSM):

    def __init__(self, screen, ai_controller, state=FsmState.Idle):
        super().__init__(screen, ai_controller, state)
