#!/usr/bin/python3

import pygame as pg
import random
from pygame.locals import *

from utils import event
from  enum import Enum

class Direction(Enum):
	UP = 0
	DOWN = 1
	LEFT = 2
	RIGHT = 3

class Snake(object):
	score      = 0
	length     = None
	direction  = None
	body 	   = None
	block_size = None
	color      = (255,255,255)
	bounds 	   = None

	def __init__(self, block_size, bounds, listener):
		self.block_size = block_size
		self.bounds	    = bounds
		self.listener   = listener
		self.respawn()

	def respawn(self):
		self.score = 0
		self.length = 3
		self.body = [(20, 20), (20, 20), (20, 20)]
		self.direction = Direction.RIGHT

	def draw(self, game, window):
		for segment in self.body:
			game.draw.rect(
				window,
				self.color,
				(segment[0], segment[1],
				self.block_size,
				self.block_size
				)
			)

	def move(self):
		curr_head = self.body[-1]
		if self.direction == Direction.DOWN:
			next_head = (curr_head[0], curr_head[1] + self.block_size)
			self.body.append(next_head)
		if self.direction == Direction.UP:
			next_head = (curr_head[0], curr_head[1] - self.block_size)
			self.body.append(next_head)
		if self.direction == Direction.RIGHT:
			next_head = (curr_head[0] + self.block_size, curr_head[1])
			self.body.append(next_head)
		if self.direction == Direction.LEFT:
			next_head = (curr_head[0] - self.block_size, curr_head[1])
			self.body.append(next_head)

		if self.length < len(self.body):
			self.body.pop(0)

	def steer(self, direction):
		if self.direction == Direction.DOWN and direction != Direction.UP:
			self.direction = direction
		if self.direction == Direction.UP and direction != Direction.DOWN:
			self.direction = direction
		if self.direction == Direction.LEFT and direction != Direction.RIGHT:
			self.direction = direction
		if self.direction == Direction.RIGHT and direction != Direction.LEFT:
			self.direction = direction

	def eat(self):
		self.length += 1
		self.score += 1

	def check_for_food(self, food):
		head = self.body[-1]
		if head[0] == food.x and head[1] == food.y:
			self.eat()
			food.respawn()

	def check_tail_collision(self):
		head = self.body[-1]
		has_eaten_tail = False

		for i in range(len(self.body) - 1):
			segment = self.body[i]
			if head[0] == segment[0] and head[1] == segment[1]:
				has_eaten_tail = True

		return has_eaten_tail

	def check_bounds(self):
		head = self.body[-1]
		
		if head[0] >= self.bounds[0]:
			return True
		if head[1] >= self.bounds[1]:
			return True
		
		if head[0] < 0:
			return True
		if head[1] < 0:
			return True

		return False

class Food(object):
	block_size = None
	color 	   = (0, 255, 0)
	x          = 100
	y          = 100
	bounds     = None

	def __init__(self, block_size, bounds):
		self.block_size = block_size
		self.bounds     = bounds

	def draw(self, game, window):
		game.draw.rect(
			window,
			self.color,
			(
				self.x,
				self.y,
				self.block_size,
				self.block_size
			)
		)

	def respawn(self):
		blocks_in_x = (self.bounds[0]/self.block_size)
		blocks_in_y = (self.bounds[1]/self.block_size)
		self.x = random.randint(0, blocks_in_x - 1) * self.block_size
		self.y = random.randint(0, blocks_in_y - 1) * self.block_size
