# encoding=utf-8
import logging

import pygame

from config.game_config import GameConfig
from fsm.fsm_machine import FSMMachine
from game_event.game_event import GameEvent

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def start_game(fsm: FSMMachine):
    clock = pygame.time.Clock()
    while True:
        clock.tick(GameConfig.fps)
        fsm.update_machine()


# 初始化游戏界面
def init_game():
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption("plane fight")
    game_display = pygame.display.set_mode(GameConfig.screen.size)
    # 敌机出场定时器
    pygame.time.set_timer(GameEvent.enemy_enter, GameConfig.enemy_enter_speed)
    return FSMMachine(game_display)


# 程序入口
if __name__ == "__main__":
    game = init_game()
    start_game(game)
    logger.info('游戏启动...')
