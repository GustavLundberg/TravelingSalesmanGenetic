import random
#from numpy.random import uniform
from Cities import *


class Chromosome():

	def __init__(self, num_cities, randomize = True, chromosome = []):
		self.num_cities = num_cities
		if randomize:
			self.chromosome = random.sample(range(num_cities), num_cities)
		else:
			self.chromosome = chromosome

	def __repr__(self):
		return str(self.chromosome)

	def getChromosome(self):
		return self.chromosome

	def plotOne(self, cities):
		cities_sorted = [cities.getCities()[i] for i in self.chromosome]
		cities_sorted.append(cities_sorted[0]) # Add the first city in the end to make sure a closed loop is plotted
		max_x = cities_sorted[0].getMax_x()
		max_y = cities_sorted[0].getMax_y()
		x_coord = [city.getX() for city in cities_sorted]
		y_coord = [city.getY() for city in cities_sorted]
		plt.plot(x_coord, y_coord, 'ro')
		plt.plot(x_coord, y_coord, 'b-')
		plt.axis([0, max_x, 0, max_y])

	def distance(self, city1, city2):
		return round(math.sqrt((city1.getX() - city2.getX()) ** 2 + (city1.getY() - city2.getY()) ** 2), 2)

	def mutate(self):
		r1 = random.randint(0, self.num_cities-1)
		r2 = random.randint(0, self.num_cities-1)
		self.chromosome[r1], self.chromosome[r2] = self.chromosome[r2], self.chromosome[r1]
		return


	def fitness(self, cities):
		cities_sorted = [cities.getCities()[i] for i in self.chromosome]
		return 1 / sum([self.distance(cities_sorted[i], cities_sorted[i+1]) if i+1 < self.num_cities else self.distance(cities_sorted[i], cities_sorted[0]) for i in range(self.num_cities)])

	def breed(self, chromosome, len_intact):
		start = random.randint(0, self.num_cities-1)
		intact = self.chromosome * 2 # Repeats the intact list 2 times
		intact = intact[start:(start+len_intact)]
		remaining = [x for x in chromosome.getChromosome() if x not in intact]

		#print('intact: ', intact)

		def rotate(lst, n):
			if len(lst):
				n = n % len(lst)
			return lst[-n:] + lst[:-n]

		# Create a list lst with intact in the correct position
		lst = [-1] * self.num_cities
		lst[:len_intact] = intact
		lst = rotate(lst, start)

		# Create a list lst2 with remaining in the correct position
		lst2 = [-1] * self.num_cities
		len_remaining = len(remaining)
		lst2[:len_remaining] = remaining
		lst2 = rotate(lst2, start + len_intact)

		#print('lst : ', lst)
		#print('lst2 : ', lst2)
		chromosome = [tup[0] if tup[0] != -1 else tup[1] for tup in zip(lst, lst2)] # Note that this is not an instance
		# of the Chromosome class, it is a list
		#print('IMPORTANT (should be type Chromosome) : ', type(a), a)
		child = Chromosome(self.num_cities, randomize = False, chromosome = chromosome) # Create a new instance of Chromosome
		return child

#c1 = Chromosome(num_cities = 5,  randomize = False, chromosome = [1, 4, 0, 2, 3])
#c2 = Chromosome(num_cities = 5,  randomize = False, chromosome = [2, 3, 1, 4, 0])

#c1 = Chromosome(num_cities = 10)
#c2 = Chromosome(num_cities = 10)

#print(c1.breed(c2, 3))
#print(c1.getChromosome())
#c1.mutate()
#print(c1.getChromosome())

#intact = [4, 0, 2]
#num_cities = 6
#a = [x for x in range(num_cities) if x != 3]
#print(a)


#c1 = [1, 4, 0, 2, 3, 5]
#c2 = [2, 3, 1, 4, 5, 0]

#cc = [, 4, 0, 2, , ] - 135
#	  [4, 0, 2]
#     [3, 1, 5]
#     [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
