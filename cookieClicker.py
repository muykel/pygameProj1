import pygame, math
from pygame.locals import *

# figure out how to count seconds in game

pygame.init()
# FPS = 15
start_time = 0
button_start_time = 0
clock = pygame.time.Clock()
mainScreen = pygame.display.set_mode([300, 300])
pygame.display.set_caption('Cookie Clicker')
# cookie = pygame.image.load('cookiez.png')
cookie2 = pygame.image.load('cookiez2.png')

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    mainScreen.fill((0, 100, 255))
    mainScreen.blit(cookie2, (640,375))
    pygame.display.update() 
    #if(start_time%1000 == 0):
    #start_time = pygame.time.get_ticks()
    #print(math.trunc(start_time/1000)) # 1 tick = 1 millisecond
    #print(start_time/1000)
    if(not float(start_time/1000).is_integer()):
        print(start_time)