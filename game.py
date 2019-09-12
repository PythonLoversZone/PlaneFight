# encoding=utf-8
import logging
import sys

import pygame
from pygame import event

from config.game_config import GameConfig, Colors

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def start_game():
    while True:
        for e in event.get():
            "用户按下了关闭游戏的按钮"
            if e.type == pygame.QUIT:
                exit_game()
            "用户按键操作"
            if e.type == pygame.KEYDOWN:
                handler()


# 事件处理
def handler():
    if event.key == pygame.K_a:
        logger.info('pressed a ')
    elif event.key == pygame.K_d:
        logger.info('pressed d ')


# 退出游戏
def exit_game():
    pygame.quit()
    sys.exit()


# 初始化游戏界面
def init_game():
    pygame.init()
    pygame.display.set_caption("plane fight")
    clock = pygame.time.Clock()
    clock.tick(GameConfig.fps)
    game_display = pygame.display.set_mode(GameConfig.screen.size)
    pygame.draw.rect(game_display, Colors.black, GameConfig.screen)
    pygame.display.update()


# 程序入口
if __name__ == "__main__":
    init_game()
    start_game()
