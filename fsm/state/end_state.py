from fsm.fsm import FSM, FsmState


# 游戏结束状态 显示当前分数和重新开始按钮
class EndState(FSM):

    def __init__(self, screen, ai_controller, state=FsmState.End):
        super().__init__(screen, ai_controller, state)
