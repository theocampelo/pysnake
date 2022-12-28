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

				if event.key == pg.K_w:
					self.key_pressed = pg.K_w
				if event.key == pg.K_a:
					self.key_pressed = pg.K_a
				if event.key == pg.K_s:
					self.key_pressed = pg.K_s
				if event.key == pg.K_d:
					self.key_pressed = pg.K_d