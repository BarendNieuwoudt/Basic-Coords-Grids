import math

class BasicCoordinate:

	def __init__(self, x, y, icon = 'x'):
		self.x = x
		self.y = y
		self.icon = icon
		
	def setCoordinates(self, x, y):
		self.x = x
		self.y = y
		
	def setX(self, x):
		self.x = x
	
	def getX(self):
		return self.x
	
	def setY(self, y):
		self.y = y
		
	def getY(self):
		return self.y
		
	def setIcon(self, icon):
		self.icon = icon
		
	def getIcon(self):
		return self.icon
	
	# Calculate absolute distance form the current coord to the given coord, rounder to 1 decimal place. 
	def distanceFrom(self, coordinate):
		diffX = (self.getX() - coordinate.getX())
		diffY = (self.getY() - coordinate.getY())
		return abs(round(math.sqrt(math.pow(diffX, 2) + math.pow(diffY, 2)), 1))
		
	def equals(self, coordinate):
		return self.x == coordinate.getX() and self.y == coordinate.getY()
		
	def __str__(self):
		return str(self.x) + ' ' + str(self.y)