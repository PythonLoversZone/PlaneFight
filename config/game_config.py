"""游戏配置"""
import random

import pygame
from pygame.rect import Rect


class GameConfig:
    player_attack_speed = 0.5
    enemy_enter_speed = random.randint(1000, 3000)
    player_move_speed = 3
    # (left,top) (width,height)
    screen = Rect((0, 0), (480, 700))
    enemy_move_speed = random.randint(1, 3)
    enemy_attack_speed = 1
    fps = 60


class Colors:
    red = (255, 0, 0)
    white = (255, 255, 255)
    black = (0, 0, 0)


"""所有的图片资源"""


class Resource:
    player = 'images/me1.png'
    start_game = 'images/game_start.png'
    restart_game = 'images/game_restart.png'
    gameOver = 'images/gameover.png'
    enemy1 = 'images/enemy1.png'
    enemy2 = 'images/enemy2.png'
    background = 'images/background.png'
    bullet = 'images/bullet'
    pause = 'images/pause_nor.png'

    @staticmethod
    def create_image(image):
        return pygame.image.load(image).convert()
