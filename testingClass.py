import pygame
from pygame.locals import *

# next time make rinp and laserp objects instead of using them all as global variables

pygame.init()
display_x, display_y = 500, 500
mainScreen = pygame.display.set_mode([display_x, display_y])
pygame.display.set_caption('Testing Window')
icon = pygame.image.load('dragonicon.png')
pygame.display.set_icon(icon)
rinp = pygame.image.load('rinp_1_29.png')
laserp = pygame.image.load('red-beam-png-2_12.png')

# rinp = sprite

global xval, yval
xval, yval = 75, 75

global xlas, ylas
xlas = xval+130
ylas = yval+40

class spriteInfo:
    def __init__(self, xcoord, ycoord, img):
        self.xcoord = xcoord
        self.ycoord = ycoord
        self.img = img
    def getx(var):
        return var.xcoord

def moveImg(val, dir):
    global xval
    global yval
    global xlas
    global ylas
    if(dir.lower()=="x"):
        xval+=val
        ylas+=val
    elif(dir.lower()=="y"):
        yval+=val
        ylas+=val

def shootLaser():
    global xval
    global yval
    global xlas
    global ylas
    xlas = xval+130
    ylas = yval+40
    for i in range(50):
        xlas+=5
        mainScreen.blit(laserp, (xlas, ylas))
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
    mainScreen.blit(rinp, (xval, yval))
    pygame.display.update() 

