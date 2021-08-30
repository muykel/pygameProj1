import pygame, math
from pygame.locals import *

pygame.init()
# FPS = 15
start_time = pygame.time.get_ticks() # first tick
button_start_time = 0
clock = pygame.time.Clock()
mainScreen = pygame.display.set_mode([300, 300])
pygame.display.set_caption('Testing Window')
a = pygame.image.load('dragonicon.png')
pygame.display.set_icon(a)
# cookie = pygame.image.load('cookiez2.png')

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    mainScreen.fill((0, 100, 255))
    # mainScreen.blit(cookie2, (640,375))
    pygame.display.update() 
    # start_time = pygame.time.get_ticks()
    # for i in range(10):
    #     pygame.time.wait(1000)
    #     print(i)