from sys import exit

import pygame
from pygame.locals import *

import constants

__author__ = 'Zygimantus'

screen = pygame.display.set_mode(constants.SCREEN_SIZE, 0, 32)
pygame.display.set_caption(constants.CAPTION)
pygame.init()

while True:
    event = pygame.event.wait()

    if event.type == QUIT:
        exit()