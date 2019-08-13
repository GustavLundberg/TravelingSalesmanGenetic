import matplotlib.pyplot as plt
#from City import *
from statistics import mean
from Cities import *
from Chromosomes import *


def plotBest(chromosome, cities, num_generations, curr_generation, curr_plot, plot_every_nth_generation):
	plt.subplot(int(math.sqrt(num_generations) / plot_every_nth_generation) + 7, int(math.sqrt(num_generations) / plot_every_nth_generation) + 7, curr_plot + 1, aspect='equal')
	plt.subplots_adjust(hspace = 0.5)
	#matplotlib.pyplot.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=None)[source]
	plt.title('Gen: ' + str(curr_generation))
	chromosome.plotOne(cities)

# Parameters
num_cities = 100                                                       # 16 # 80
population_size = 1000                                                # 1000
max_x = 1000 
max_y = 1000
num_generations = 6000                                                # 200 # 1000
len_intact = 16 # Parameter related to the breeding process            # 8
mutate_probability = 0.5                                              # 0.1
reduce_factor = 20                                                     # 100
increase_factor = 2
scaling_reduce_factor = 1.01                                         # 1.00
scaling_increase_factor = 1.001                                         # 1.005 or 1.01
num_mutations = 10                                                      # 1
plot_generations = False
plot_every_nth_generation = 200 # Plot only every nth generation

# Initialize cities and the first population of chromosomes
cities = Cities(num_cities, max_x, max_y)
chromosomes = Chromosomes(num_cities, population_size)

#print('gen0 : ', chromosomes.getChromosomes())
#print('type : ', type(chromosomes))
#chromosomes.calculateFitness(cities)
#chromosomes.sortPopulation()
#print('fitness, gen0 : ', chromosomes.getFitness())

fitness_history = []
distance_history = []
best_fitness = 0
best_gen = 0
count_plots = 0
for i in range(num_generations):
	print('Gen ' + str(i) + ' out of ' + str(num_generations))
	chromosomes.calculateFitness(cities)
	fitness_history.append(mean(chromosomes.getFitness()))
	distance_history.append(1/mean(chromosomes.getFitness()))
	chromosomes.sortPopulation()
	# Find the best chromosome ni all generations
	if chromosomes.getFitness()[0] > best_fitness: # Note that getFitness gives you the distance, i.e. a low fitness is equal to a good result
		best_fitness = chromosomes.getFitness()[0]
		best_chromosome = chromosomes.getChromosomes()[0] # Save the best chromosome
		best_gen = i

	if plot_generations and i % plot_every_nth_generation == 0:
		plt.figure(1)
		plotBest(chromosome = chromosomes.getChromosomes()[0], cities = cities, 
			num_generations = num_generations, curr_generation = i, curr_plot = count_plots, plot_every_nth_generation = plot_every_nth_generation)
		count_plots += 1
	if i < num_generations-1:
		chromosomes.breedPopulationAndUpdateCurrentPopulation(len_intact = len_intact, population_size = population_size, 
			reduce_factor = reduce_factor, increase_factor = increase_factor)
		chromosomes.mutateGeneration(probability = mutate_probability, num_mutations = num_mutations)
		reduce_factor += reduce_factor*scaling_reduce_factor
		increase_factor = increase_factor*scaling_increase_factor # Increase the increase factor with #1 %# each iteration
		#print('increase_factor = ', increase_factor)

# Plots the best chromosome in all generations
plt.figure(10)
plt.title('Best solution came from generation : ' + str(best_gen))
best_chromosome.plotOne(cities)

# Plots last generation
plt.figure(2)
plt.title('Best solution from last generation')
chromosomes.getChromosomes()[0].plotOne(cities)
#plotBest(chromosome = chromosomes.getChromosomes()[0], cities = cities, 
#		num_generations = num_generations, curr_generation = num_generations-1)

plt.figure(3)
plt.xlabel('Generation')
plt.ylabel('Average distance')
plt.title('Average distance')
plt.plot(list(range(num_generations)), distance_history)
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