import pygame
import math
from pygame.locals import *

pygame.init()
display_x, display_y = 500, 500
mainScreen = pygame.display.set_mode([display_x, display_y])
pygame.display.set_caption('Testing Window')
icon = pygame.image.load('dragonicon.png')
pygame.display.set_icon(icon)
cookie = pygame.image.load('cookiez.png')

global cookieX, cookieY
cookieX = display_x * 0.45
cookieY = display_y * 0.8

def moveCookie(val, dir):
    global cookieX
    global cookieY
    if(dir.lower()=="x"):
        cookieX+=val
    elif(dir.lower()=="y"):
        cookieY+=val
    else:
        print("dimensions must on the X or Y plane")
    mainScreen.blit(cookie, (cookieX, cookieY))
    pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("spacebar was pressed")
            if event.key == pygame.K_w:
                moveCookie(-5,"y")
                print("w")
            if event.key == pygame.K_s:
                moveCookie(5,"y")
                print("s")
            if event.key == pygame.K_a:
                moveCookie(-5,"x")
                print("a")
            if event.key == pygame.K_d:
                moveCookie(5,"x")
                print("d")
    mainScreen.fill((0, 100, 255))
    mainScreen.blit(cookie, (0, 0))
    pygame.display.update() 

