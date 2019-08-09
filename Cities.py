import math
import matplotlib.pyplot as plt
from City import *

class Cities():

	def __init__(self, num_cities, max_x, max_y):
		self.cities = [City(max_x, max_y) for _ in range(num_cities)]
		self.num_cities = num_cities
		self.max_x = max_x
		self.max_y = max_y

	def __repr__(self):
		return str(self.cities)

	def getCities(self):
		return self.cities

	def getMax_x(self):
		return self.max_x

	def getMax_y(self):
		return self.max_y

	#def distance(self, city1, city2):
	#	return math.sqrt((city1.getX() - city2.getX()) ** 2 + (city1.getY() - city2.getY()) ** 2)

	#def totalDistance(self):
	#	return sum([self.distance(self.cities[i], self.cities[i+1]) if i+1 < self.num_cities else self.distance(self.cities[i], self.cities[0]) for i in range(self.num_cities)])

	def plotCities(self):
		x_coord = [city.getX() for city in self.cities]
		y_coord = [city.getY() for city in self.cities]
		plt.plot(x_coord, y_coord, 'ro')
		plt.axis([0, self.max_x, 0, self.max_y])
		plt.show()
