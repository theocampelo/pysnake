#!/usr/bin/python3

import sys
import os

from pygame.locals import *
from utils import screen
from utils import entity

if __name__ == '__main__':

    game   = screen.Screen(800, 600) 
    screen = game.surface
    game.start()

    running = True
    snake_body = []

    snake_size = 10
    snake = entity.Snake(screen, color, snake_body)

    while running:
        screen.fill((0,0,0))
        game.update()     # update screen e event listener