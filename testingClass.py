import pygame
import math
import config
from pygame.locals import *

pygame.init()
# FPS = 15
# start_time = pygame.time.get_ticks()
# clock = pygame.time.Clock()
mainScreen = pygame.display.set_mode([500, 500])
pygame.display.set_caption('Testing Window')
icon = pygame.image.load('dragonicon.png')
pygame.display.set_icon(icon)
cookie = pygame.image.load('cookiez.png')

cookieX = 0
cookieY = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("spacebar was pressed")
            if event.type == pygame.K_w:
                moveCookie(5,"y")
            if event.type == pygame.K_s:
                moveCookie(-5,"y")
            if event.type == pygame.K_a:
                moveCookie(-5,"x")
            if event.type == pygame.K_d:
                moveCookie(5,"x")
    mainScreen.fill((0, 100, 255))

def moveCookie(val, dir):
    if(dir.lower()=="x"):
        cookieX+=val
    elif(dir.lower()=="y"):
        cookieY+=val
    else:
        print("dimensions must on the X or Y plane")
    mainScreen.blit(cookie, (cookieX, cookieY))
    pygame.display.update() 