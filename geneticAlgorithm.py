import random
from phrase import Phrase, target
from helpers import summarize

class Genetic:
# prompt the user for a generation size
    user_input_str = input("Please enter a generation size: ")
    popSize = int(user_input_str)

# keep track of the population, generation, and the best score we've seen so far
    generation = 1
    bestScore = 0

# create initial population from which other generation will follow
    population = []
    for i in range(popSize):
       # sentence = chr(random.choice(range(32, 127)))
        population.append(Phrase())
        
    
# keep going until we have found the target string
    while bestScore < len(target):

    # assess the fitness of each member of the population 
        for i in range(popSize):
            population[i].getFitness()

        # if it is the best we have seen before report it and save it
            if population[i].fitness > bestScore:
            # update the best score
                bestScore = population[i].fitness
                summarize(generation, population[i].getContents(), bestScore)


    # create the mating pool for the next generation
        matingPool = []

    # clear the population array but save the parents
        parents = population[:]
        population = []

    # for each one of the parents, add it to the mating pool more often if their fitniss is higher
        for i in range(popSize):
            for j in range(parents[i].fitness):
                matingPool.append(parents[i])

    # build the next generation

        # arbitrarily choose two parents from the mating pool
    
        for i in range(popSize):
            parent1 = random.choice(matingPool)
            parent2 = random.choice(matingPool)

            # crossoer the two parents
            child = Phrase.crossOver(parent1, parent2)

            # small chance that some of the characters will mutate
            Phrase.mutate(child)

            # add the child to the next generation's population
            population.append(child)



        # done assessing the currents generation and move onto the next one
        generation = generation + 1