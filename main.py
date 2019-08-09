import matplotlib.pyplot as plt
#from City import *
from statistics import mean
from Cities import *
from Chromosomes import *


def plotBest(chromosome, cities, num_generations, curr_generation):
	plt.subplot(int(math.sqrt(num_generations)) + 1, int(math.sqrt(num_generations)) + 1, curr_generation + 1, aspect='equal')
	plt.subplots_adjust(hspace = 0.5)
	#matplotlib.pyplot.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=None)[source]
	plt.title('Gen: ' + str(curr_generation))
	chromosome.plotOne(cities)


# Parameters
num_cities = 11
population_size = 1200
max_x = 1000
max_y = 1000
num_generations = 60
len_intact = 5 # Parameter related to the breeding process

# Initialize cities and the first population of chromosomes
cities = Cities(num_cities, max_x, max_y)
chromosomes = Chromosomes(num_cities, population_size)
#print('gen0 : ', chromosomes.getChromosomes())
#print('type : ', type(chromosomes))
#chromosomes.calculateFitness(cities)
#chromosomes.sortPopulation()
#print('fitness, gen0 : ', chromosomes.getFitness())

fitness_history = []

plt.figure(1)
for i in range(num_generations):
	print('Gen ' + str(i) + ' out of ' + str(num_generations))
	chromosomes.calculateFitness(cities)
	fitness_history.append(mean(chromosomes.getFitness()))
	#print('fitness: ', chromosomes.getFitness(), type(chromosomes.getFitness()))
	#print('fitness, gen', i, mean(chromosomes.getFitness()))
	chromosomes.sortPopulation()
	plotBest(chromosome = chromosomes.getChromosomes()[0], cities = cities, 
		num_generations = num_generations, curr_generation = i)
	if i < num_generations-1:
		chromosomes.breedPopulationAndUpdateCurrentPopulation(len_intact = len_intact, population_size = population_size)

# Plotting last generation
plt.figure(2)
chromosomes.getChromosomes()[0].plotOne(cities)
#plotBest(chromosome = chromosomes.getChromosomes()[0], cities = cities, 
#		num_generations = num_generations, curr_generation = num_generations-1)

plt.figure(3)
plt.xlabel('Generations')
plt.ylabel('Average fitness')
plt.plot(list(range(num_generations)), fitness_history)
plt.show()

#chromosomes.getChromosomes()[0].plot(cities)

#x = [c.getX() for c in cities.getCities()]
#y = [c.getY() for c in cities.getCities()]
#plt.plot(x, y, 'ro-')
#plt.show()


#print('children : ', chromosomes.breedPopulation(3, population_size))
#chromosomes.breedPopulationAndUpdateCurrentPopulation(len_intact = 3, population_size = population_size)
#print('gen1 : ', chromosomes.getChromosomes())
#print('type : ', type(chromosomes))
#chromosomes.calculateFitness(cities)
#chromosomes.sortPopulation()
#print('fitness, gen1 : ', chromosomes.getFitness())



#print('Before: ', chromosomes.getChromosomes())
#print('Before: ', chromosomes.getFitness(cities))

# Select and print 5 chromosomes
#print([c.getChromosome() for c in chromosomes.selectChromosomes(5)])
#print(chromosomes.selectChromosomes()[0].getChromosome())

#print('child : ', chromosomes.breedPopulation(3, population_size))

#chromosomes.sortPopulation()

#print('After: ', chromosomes.getChromosomes())
#print('After: ', chromosomes.getFitness(cities))

#population = [list(tup) for tup in zip(chromosomes.getChromosomes(), fitness)]
#print(population)

# Sort according to fitness in descending order
#def fitnessKey(list_chromosome_fitness):
#	return list_chromosome_fitness[1]

#population = sorted(population, key = fitnessKey)
#print(population)