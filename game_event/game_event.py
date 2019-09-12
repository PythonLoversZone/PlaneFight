import pygame


class GameEvent:
    # 用户自定义事件
    hurt = 25
    attack = 26
    end = 27
    idle = 28
    start_game = 29

    # 以下为pygame内置事件
    pause_game = pygame.K_PAUSE
    move_left = pygame.K_a
    move_right = pygame.K_d
    quit = pygame.QUIT
