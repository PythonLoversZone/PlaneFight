import sys
import pygame

pygame.init()

red = (255, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)

pygame.display.set_caption("slither game")
game_display = pygame.display.set_mode((500, 400))
game_display.fill(white)

clock = pygame.time.Clock()

box_x = 300
box_y = 300

game_exit = False

while not game_exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_exit = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                box_x -= 25
            elif event.key == pygame.K_RIGHT:
                box_x += 25
    pygame.draw.rect(game_display, black, [box_x, box_y, 25, 25])
    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()
