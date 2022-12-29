

import pygame as pg, sys, os
from pygame.locals import *

from utils import event

class Screen(object):
	def __init__(self, bounds, listener):
		self.clock    = pg.time.Clock()
		self.bounds = pg.display.set_mode(bounds)
		self.listener = listener

	def start(self):
		pg.init()
		pg.mouse.set_visible(0)
		pg.display.set_caption('Snake by INCOMBINER[olepx]')

	def update(self):
		self.clock.tick(10)
		self.listener.handle_keys()
		pg.display.update()