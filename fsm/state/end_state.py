from fsm.fsm_state import FSMStateEnum, FSMState


# 游戏结束状态 显示当前分数和重新开始按钮
class EndState(FSMState):

    def __init__(self, screen, ai_controller):
        super().__init__(screen, ai_controller)

    def update_view(self):
        pass

    def type(self):
        return FSMStateEnum.End
