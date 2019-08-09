import random
import matplotlib.pyplot as plt
from numpy.random import choice
from Chromosome import *

class Chromosomes:

	def __init__(self, num_cities, population_size):
		self.num_cities = num_cities
		self.population_size = population_size
		self.chromosomes = [Chromosome(num_cities = num_cities, randomize = True) for _ in range(population_size)]
		self.fitness = None

	def __repr__(self):
		return str(self.chromosomes)

	def getChromosomes(self):
		return self.chromosomes

	# Plots the best chromosome for current generation. Assumes that the list of chromosomes 
	# have been sorted using sortPopulation()
	def plotBest(self, cities):
		plt.subplot()
		self.chromosomes[0].plotOne(cities)

	def calculateFitness(self, cities):
		self.fitness = [c.fitness(cities) for c in self.chromosomes]
		return

	def getFitness(self):
		return self.fitness

	def sortPopulation(self):
		population = [tup for tup in zip(self.chromosomes, self.fitness)]

		# Sort according to fitness in descending order
		def fitnessKey(tuple_chromosome_fitness):
			return tuple_chromosome_fitness[1] # Sorting by the second element of the tuple

		population = sorted(population, key = fitnessKey)
		self.chromosomes = [tup[0] for tup in population]
		self.fitness = [tup[1] for tup in population]
		return

	def selectChromosomes(self, num):
		p = [1/f_outer *  1/sum([1/f_inner for f_inner in self.fitness]) for f_outer in self.fitness]
		# Select one chromosome by randomly sampling an integer with weights being 1 / fitness (and then normalizing p, making sure it sums to one)
		rand_ints = choice(list(range(self.population_size)), num, 
			p = [1/f_outer *  1/sum([1/f_inner for f_inner in self.fitness]) for f_outer in self.fitness])
		return [self.chromosomes[i] for i in rand_ints]

	def breedPopulation(self, len_intact, population_size):
		parents = self.selectChromosomes(population_size * 2) # 2 parents create one child
		parent0 = parents[0]
		parent1 = parents[1]
		#print('parent0 : ', type(parent0), parent0)
		#print('parent1 : ', type(parent1), parent1)
		child = parents[0].breed(parents[1], len_intact)
		children = [parents[i].breed(parents[i+1], len_intact) if i+1 < 2*population_size 
			else parents[i].breed(parents[0], len_intact) 
			for i in range(0, population_size * 2, 2)]
		return children

	def breedPopulationAndUpdateCurrentPopulation(self, len_intact, population_size):
		children = self.breedPopulation(len_intact, population_size)
		#print('children (breedPopulationAndUpdateCurrentPopulation)', type(children), children)
		self.chromosomes = children
		return


