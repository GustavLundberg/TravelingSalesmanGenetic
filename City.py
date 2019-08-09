import random

class City:
	
	def __init__(self, max_x, max_y):
		self.x = int(random.uniform(0, max_x))
		self.y = int(random.uniform(0, max_y))
		self.max_x = max_x
		self.max_y = max_y

	def __repr__(self):
		return str((self.x, self.y))

	def getX(self):
		return self.x

	def getY(self):
		return self.y

	def getMax_x(self):
		return self.max_x

	def getMax_y(self):
		return self.max_y