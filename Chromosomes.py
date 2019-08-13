import random
import matplotlib.pyplot as plt
from numpy.random import choice, uniform
from statistics import mean
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
#	def plotBest(self, cities):
#		plt.subplot()
#		self.chromosomes[0].plotOne(cities)

	def calculateFitness(self, cities):
		self.fitness = [c.fitness(cities) for c in self.chromosomes]
		return

	def getFitness(self):
		return self.fitness

	# Swaps two random genes with some probability
	def mutateGeneration(self, probability = 0.1, num_mutations = 1):
		for i in range(num_mutations):
			probs = uniform(size = self.population_size)
			for tup in zip(probs, self.chromosomes):
				if tup[0] < probability:
					tup[1].mutate()
		return

	def sortPopulation(self):
		population = [tup for tup in zip(self.chromosomes, self.fitness)]

		# Sort according to fitness in descending order
		def fitnessKey(tuple_chromosome_fitness):
			return tuple_chromosome_fitness[1] # Sorting by the second element of the tuple

		population = sorted(population, key = fitnessKey, reverse = True)
		self.chromosomes = [tup[0] for tup in population]
		self.fitness = [tup[1] for tup in population]
		return

	def selectChromosomes(self, num, reduce_factor = 100, increase_factor = 2):
		min_fitness = min(self.fitness)
		max_fitness = max(self.fitness)
		p_normalized = [f/max_fitness for f in self.fitness] # Normalizing so that elements in list are between 0 and 1
		
		# Making the probability weights of the chromosomes with a fitness of less than the average fitness smaller - Makes a huge difference!!!
		avg = mean(p_normalized)
		p_normalized = [e / reduce_factor if e < avg else e for e in p_normalized] # / 1000
		p_normalized = [e / (reduce_factor*10) if e < sorted(p_normalized, reverse = False)[int(self.population_size / 10)] else e for e in p_normalized] # / 1000
		# Make the weight larger if a chromosome has a larger fitness than 90 % of the other chromosomes
		p_normalized = [e * increase_factor if e > sorted(p_normalized, reverse = True)[int(self.population_size / 10)] else e for e in p_normalized] # e * 2, /10
		p_normalized = [e * increase_factor * 100 if e > sorted(p_normalized, reverse = True)[int(self.population_size / 100)] else e for e in p_normalized] # e * 5, /100


		#print('---------------', p_normalized)
		#print('p_temp', p_temp)
		p = [f_outer *  1/sum([f_inner for f_inner in p_normalized]) for f_outer in p_normalized]


		#p = [1/f_outer *  1/sum([1/f_inner for f_inner in self.fitness]) for f_outer in self.fitness]
		# Select one chromosome by randomly sampling an integer with weights being 1 / fitness (and then normalizing p, making sure it sums to one)
		
		#rand_ints = choice(list(range(self.population_size)), num, 
		#	p = [1/f_outer *  1/sum([1/f_inner for f_inner in self.fitness]) for f_outer in self.fitness])
		rand_ints = choice(list(range(self.population_size)), num, 
			p = p)

		#print('p', p)
		return [self.chromosomes[i] for i in rand_ints]

	def breedPopulation(self, len_intact, population_size, reduce_factor = 100, increase_factor = 2):
		parents = self.selectChromosomes(num = population_size * 2, reduce_factor = 100, increase_factor = 2) # 2 parents create one child
		parent0 = parents[0]
		parent1 = parents[1]
		#print('parent0 : ', type(parent0), parent0)
		#print('parent1 : ', type(parent1), parent1)
		child = parents[0].breed(parents[1], len_intact)
		children = [parents[i].breed(parents[i+1], len_intact) if i+1 < 2*population_size 
			else parents[i].breed(parents[0], len_intact) 
			for i in range(0, population_size * 2, 2)]
		return children

	def breedPopulationAndUpdateCurrentPopulation(self, len_intact, population_size, reduce_factor = 100, increase_factor = 2):
		children = self.breedPopulation(len_intact = len_intact, population_size = population_size, reduce_factor = 100, increase_factor = 2)
		#print('children (breedPopulationAndUpdateCurrentPopulation)', type(children), children)
		self.chromosomes = children
		return


