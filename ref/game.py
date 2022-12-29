#!/usr/bin/python3

import pygame as pg
import sys
import os

from pygame.locals import *
from utils import screen
from utils import entity
from utils import event

if __name__ == '__main__':

    pg.font.init()
    font = pg.font.Font('fonts/LiberationMono-Regular.ttf', 30)

    bounds   = (300, 300)
    listener = event.Listener()
    screen   = screen.Screen(bounds, listener)
    window   = screen.bounds

    screen.start()

    gameover = False

    block_size = 10
    snake = entity.Snake(block_size, bounds, screen.listener)
    food  = entity.Food(block_size, bounds)

    # Game Loop
    while not gameover:
        if listener.key_pressed == pg.K_w:
            snake.steer(snake.direction.UP)
        if listener.key_pressed == pg.K_a:
            snake.steer(snake.direction.LEFT)
        if listener.key_pressed == pg.K_s:
            snake.steer(snake.direction.DOWN)
        if listener.key_pressed == pg.K_d:
            snake.steer(snake.direction.RIGHT)

        snake.move()
        snake.check_for_food(food)

        if snake.check_bounds() == True or snake.check_tail_collision() == True:
            #text = font.render('Game Over', True, (255,255,255))
            #screen.bounds.blit(text, (20,120))
            screen.update()
            snake.respawn()
            food.respawn()

        window.fill((0,0,0))

        food.draw(pg, window)
        snake.draw(pg, window)
        screen.update()     # update screen e event listener