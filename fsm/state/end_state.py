from fsm.fsm_machine import FSMMachine
from fsm.fsm_state import FSMStateEnum


# 游戏结束状态 显示当前分数和重新开始按钮
class EndState(FSMMachine):

    def __init__(self, screen, ai_controller, state=FSMStateEnum.End):
        super().__init__(screen, ai_controller, state)
