import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

pygame.init()

mainScreen = pygame.display.set_mode([1280, 800])

running = True
while running:
    # Code to quit the app
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
