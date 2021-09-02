import pygame
from pygame.locals import *

pygame.init()

display_x, display_y = 500, 500
xval, yval = 75, 75
mainScreen = pygame.display.set_mode([display_x, display_y])
pygame.display.set_caption('Testing Window')
rinpic = pygame.image.load('rinp_1_29.png')
laserpic = pygame.image.load('red-beam-png-2_12.png')
iconpic = pygame.image.load('dragonicon.png')
pygame.display.set_icon(iconpic)

class spriteInfo:
    def __init__(self, xcoord, ycoord):
        self.xcoord = xcoord
        self.ycoord = ycoord

    def change_x(self, val):
        self.xcoord+=val
        
    def change_y(self, val):
        self.ycoord+=val

rinp = spriteInfo(xval, yval)
laserp = spriteInfo(xval + 130, yval + 40)

def moveImg(val, dir):
    if(dir.lower()=="x"):
        rinp.change_x(val)
    elif(dir.lower()=="y"):
        rinp.change_y(val)

def shootLaser():
    laserp.xcoord = rinp.xcoord + 130
    laserp.ycoord = rinp.ycoord + 40
    for i in range(50):
        laserp.change_x(5)
        mainScreen.blit(laserpic, (laserp.xcoord, laserp.ycoord))
        pygame.display.update() 
        pygame.time.wait(3)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                shootLaser()
            if event.key == pygame.K_w:
                moveImg(-5,"y")
            if event.key == pygame.K_s:
                moveImg(5,"y")
            if event.key == pygame.K_a:
                moveImg(-5,"x")
            if event.key == pygame.K_d:
                moveImg(5,"x")
    mainScreen.fill((0, 150, 255))
    mainScreen.blit(rinpic, (rinp.xcoord, rinp.ycoord))
    pygame.display.update()