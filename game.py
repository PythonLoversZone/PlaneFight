# encoding=utf-8
import logging

import pygame

from config.game_config import GameConfig
from fsm.ai.idle_ai import IdleAI
from fsm.fsm_machine import FSMMachine
from game_event.game_event import GameEvent

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def start_game(fsm: FSMMachine):
    while True:
        fsm.update()


# 初始化游戏界面
def init_game():
    pygame.init()
    pygame.display.set_caption("plane fight")
    clock = pygame.time.Clock()
    clock.tick(GameConfig.fps)
    game_display = pygame.display.set_mode(GameConfig.screen.size)

    # 注册用户自定义事件
    pygame.time.set_timer(GameEvent.hurt, GameConfig.fps)
    pygame.time.set_timer(GameEvent.attack, GameConfig.fps)
    # pygame.time.set_timer(GameEvent.end, GameConfig.fps)
    # pygame.time.set_timer(GameEvent.idle, GameConfig.fps)
    # pygame.time.set_timer(GameEvent.start_game, GameConfig.fps)

    return FSMMachine(game_display, IdleAI())


# 程序入口
if __name__ == "__main__":
    game = init_game()
    start_game(game)
