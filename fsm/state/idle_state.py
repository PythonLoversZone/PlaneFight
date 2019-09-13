from fsm.fsm_state import FSMStateEnum, FSMState


# 初始状态 仅一个背景和一个开始按钮
class IdleState(FSMState):

    def __init__(self, screen, ai_controller):
        super().__init__(screen, ai_controller)

    def enter(self):
        super().enter()

    def type(self):
        return FSMStateEnum.Idle

    def update_view(self):
        super().update_view()
        self.back_group.update()
        self.back_group.draw(self.screen)
