#XOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXO
# Name: Mohammad BoAisha
# Lab Sec: 226
# P5
#XOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXO

import random

#XOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXO
#XOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXO
#A representation of the Tile (A None tile is the empty space)
class Tile:
	#The value of the tile, initially None
	value = None
	def __init__(self,value):
		self.value = value
	#Prints the value
	def __str__(self):
		if self.value == None:
			return "<>"
		else:
			return str(self.value)
	#Computer-centric view
	def __repr__(self):
		return "Tile({0})".format(value)

#XOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXO
#XOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXO
class Direction:
	value = None
	def __init__(self,value):
		pass
	def __str__(self):
		pass
	def __repr__(self):
		pass
	def __eq__(self,other):
		pass
#XOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXO
#XOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXO
UP	= Direction("UP")
DOWN = Direction("DOWN")
LEFT = Direction("LEFT")
RIGHT = Direction("RIGHT")
dirs = [UP,DOWN,LEFT,RIGHT]
#XOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXO
#XOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXO
class TileError(Exception):
	msg = None
	def __init__(self,msg):
		pass
	def __str__(self):
		pass
	def __repr__(self):
		pass
#XOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXO
#XOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXO
class Puzzle:
	grid = None
	def __init__(self, grid=None,height=4,width=4):
		pass
	def __str__(self):
		pass
	def __repr__(self):
		pass
	def display(self):
		pass
	def find_opening(self):
		pass
	def move(self, dir):
		pass
	def is_solved(self):
		pass
	def scramble(self, n=1000):
		pass
	
