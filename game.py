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

    boundy   = 300
    boundx   = 300
    bounds   = (boundy, boundx)
    listener = event.Listener()
    screen   = screen.Screen(bounds, listener)
    window   = screen.bounds
    i = 0

    screen.start()

    gameover = False

    block_size = 10
    snake = entity.Snake(block_size, bounds, screen.listener)
    food  = entity.Food(block_size, bounds)

    first_update = False

    # Game Loop
    while not gameover:

        score_text = font.render(f'Score: {snake.score}', True, (255,255,255))
        screen.bounds.blit(score_text, (5, 5))

        if listener.key_pressed == pg.K_UP:
            snake.steer(snake.direction.UP)
        if listener.key_pressed == pg.K_LEFT:
            snake.steer(snake.direction.LEFT)
        if listener.key_pressed == pg.K_DOWN:
            snake.steer(snake.direction.DOWN)
        if listener.key_pressed == pg.K_RIGHT:
            snake.steer(snake.direction.RIGHT)

        snake.move()
        snake.check_for_food(food)

        if snake.check_bounds() == True or snake.check_tail_collision() == True:
            text = font.render('Game Over', True, (255,255,255))

            text_rect = text.get_rect(center = (boundy/2,boundx/2))
            screen.bounds.blit(text, text_rect)
            screen.update()

            pg.time.delay(1000)
            snake.respawn()
            food.respawn()

        window.fill((50,50,50))

        food.draw(pg, window)
        snake.draw(pg, window)

        if i == 0:
            screen.update()
            pg.event.wait()
            print("WAIT")
            i += 1
        elif i != 0:
            screen.update()