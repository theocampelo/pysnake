#!/usr/bin/python3

import pygame as pg
from pygame.locals import *

from utils import event

class Snake(object):
	def __init__(self, screen, color, snake_body, snake_size):
		self.screen 	= screen
		self.color		= color
		self.snake_body = snake_body
		self.snake_size = snake_size

	def draw(self):
		for x in snake_body:
			pg.draw.rect(
				screen,
				color,
				snake_body,
				snake_body,
				snake_size,
				snake_size
				)