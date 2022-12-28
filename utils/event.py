#!/usr/bin/python3

import pygame as pg, sys
from pygame.locals import *

class Listener(object):
	def __init__(self):
		self.key_pressed = None

	def start(self):
		for event in pg.event.get():
			if event.type == pg.QUIT:
				sys.exit()