import pygame


class GameEvent:
    # 用户自定义事件
    hurt = pygame.USEREVENT
    attack = pygame.USEREVENT + 1
    end = pygame.USEREVENT + 2
    idle = pygame.USEREVENT + 3
    start_game = pygame.USEREVENT + 4
    enemy_enter = pygame.USEREVENT + 5

    # 以下为pygame内置事件
    pause_game = pygame.K_PAUSE
    move_left = pygame.K_a
    move_right = pygame.K_d
    quit = pygame.QUIT
    click = pygame.MOUSEBUTTONDOWN
