import pygame
# from pygame.locals import (
#     K_UP,
#     K_DOWN,
#     K_LEFT,
#     K_RIGHT,
#     K_ESCAPE,
#     KEYDOWN,
#     QUIT,
# )
pygame.init()
mainScreen = pygame.display.set_mode([1280, 800])
pygame.display.set_caption('Gabe is trash :joy:')
rinPic = pygame.image.load('rinpygame.jpeg')

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #mainScreen.fill((255, 255, 255))
    mainScreen.blit(rinPic, (300,300))
    pygame.display.update() 