#!/usr/bin/python3

import pygame as pg, sys, os
from pygame.locals import *

from utils import event

class Screen(object):
	def __init__(self, width, height):
		self.width    = width
		self.height   = height
		self.clock    = pg.time.Clock()
		self.surface  = pg.display.set_mode((self.width, self.height))
		self.listener = event.Listener()

	def start(self):
		pg.init()
		pg.mouse.set_visible(0)
		pg.display.set_caption('Snake by INCOMBINER[olepx]')

	def update(self):
		self.clock.tick(60)
		self.listener.start()
		pg.display.flip()