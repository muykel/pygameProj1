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

# figure out how to count seconds in game

pygame.init()
start_time = None
clock = pygame.time.Clock()
mainScreen = pygame.display.set_mode([1280, 750])
pygame.display.set_caption('Cookie Clicker')
cookie = pygame.image.load('cookiez.png')
cookie2 = pygame.image.load('cookiez2.png')

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    mainScreen.fill((0, 100, 255))
    mainScreen.blit(cookie2, (640,375))
    pygame.display.update() 