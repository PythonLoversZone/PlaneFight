"""游戏配置"""
from pygame.rect import Rect


class GameConfig:
    player_attack_speed = 0.5
    # (left,top) (width,height)
    screen = Rect((0, 0), (480, 700))
    enemy_move_speed = range(1, 3)
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
