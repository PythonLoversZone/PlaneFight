from fsm.fsm_machine import FSMMachine

from fsm.fsm_state import FSMStateEnum


# 初始状态 仅一个背景和一个开始按钮
class IdleState(FSMMachine):

    def __init__(self, screen, ai_controller, state=FSMStateEnum.Idle):
        super().__init__(screen, ai_controller, state)

    def enter(self):
        super().enter()
