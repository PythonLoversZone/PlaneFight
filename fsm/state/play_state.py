from fsm.fsm_machine import FSMMachine

from fsm.fsm_state import FSMStateEnum


# 运行状态
class PlayingState(FSMMachine):

    def __init__(self, screen, ai_controller, state=FSMStateEnum.Playing):
        super().__init__(screen, ai_controller, state)
