#!/usr/bin/python3

import pygame as pg, sys
from pygame.locals import *
from enum import Enum

class Listener(object):
	def __init__(self):
		self.key_pressed = None

	def handle_keys(self):
		for event in pg.event.get():
			if event.type == pg.QUIT:
				sys.exit()

			# Close when X is pressed
			if event.type == pg.KEYDOWN:
				if event.key == pg.K_x:
					print("X was pressed. Closing the game!")
					sys.exit()

				if event.key == pg.K_UP:
					self.key_pressed = pg.K_UP
				if event.key == pg.K_LEFT:
					self.key_pressed = pg.K_LEFT
				if event.key == pg.K_DOWN:
					self.key_pressed = pg.K_DOWN
				if event.key == pg.K_RIGHT:
					self.key_pressed = pg.K_RIGHT