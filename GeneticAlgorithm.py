import matplotlib.pyplot as plt
import numpy as np
import random
import math
def generate_population(size, x1, x2):
    lower_x1, upper_x1 = x1
    lower_x2, upper_x2 = x2

    population = []
    for i in range(size):
        individual = {
            "x1": random.uniform(lower_x1, upper_x1),
            "x2": random.uniform(lower_x2, upper_x2),
        }
        population.append(individual)

    return population
    
N = int(input('enter the  population size :\n'))

# define the fuction to maximize i.e. 1/(1+f^2) 
def function(individual):
    x1 = individual["x1"]
    x2 = individual["x2"]
    return 1/(1+(x1+x2-2*x1**2-x2**2+x1*x2)**2)
# define the Actual fuction for minimize 
def Actal_function(individual):
    x1 = individual["x1"]
    x2 = individual["x2"]
    return (x1+x2-2*x1**2-x2**2+x1*x2)

generations = 100
# take the inpute of x1 and x2 and size of population
population = generate_population(size=N, x1=(-15, 15), x2=(-15, 15))

i = 1
while True:
    print(f" GENERATION {i}")

    for individual in population:
        print(individual)

    if i == generations:
        break

    i += 1

    # Making next generation using roulette wheel reproduction sceme

def roulette_wheel(sorted_population, fitness):
    offset = 0
    normalized_fitness = fitness

    lowest_fitness = function(sorted_population[0])
    if lowest_fitness < 0:
        offset = -lowest_fitness
        normalized_fitness += offset * len(sorted_population)

    draw = random.uniform(0, 1)

    accumulated = 0
    for individual in sorted_population:
        
        fitness = function(individual) + offset
        probability = fitness / normalized_fitness
        accumulated += probability

        if draw <= accumulated:
            return individual

def sort_population_fitness(population):
    return sorted(population, key=function)


def crossover(individual_a, individual_b):
    x1a = individual_a["x1"]
    x2a = individual_a["x2"]

    x1b = individual_b["x1"]
    x2b = individual_b["x2"]
    
    return {"x1": (x1a + x1b) / 2, "x2": (x2a + x2b) / 2}

# enter the mutation probability 'p'
p = 0.01
def mutate(individual):
    next_x1 = individual["x1"] + random.uniform(-p, p)
    next_x2 = individual["x2"] + random.uniform(-p, p)

    lower_boundary, upper_boundary = (0, 0.5)

 
    next_x1 = min(max(next_x1, lower_boundary), upper_boundary)
    next_x2 = min(max(next_x2, lower_boundary), upper_boundary)
    
    return {"x1": next_x1, "x2": next_x2} 


def next_generation(previous_population):
    next_generation = []
    sorted_by_fitness_population = sort_population_fitness(previous_population)
    population_size = len(previous_population)
    fitness = sum(function(individual) for individual in population)

    for i in range(population_size):
        first_choice = roulette_wheel(sorted_by_fitness_population, fitness)
        second_choice = roulette_wheel(sorted_by_fitness_population, fitness)

        individual = crossover(first_choice, second_choice)
        individual = mutate(individual)
        next_generation.append(individual)

    return next_generation

generations = 100

population = generate_population(size=N, x1 = (-15, 15), x2 = (-15, 15))

i = 1
while True:
    print(f" GENERATION {i}")

    for individual in population:
        print(individual, Actal_function(individual))
    
    
    if i == generations:
        break
 
    i += 1

    population = next_generation(population)

optimal_individual = sort_population_fitness(population)[-1]
print("\n OPTIMAL SOLUTION ")
print(optimal_individual, Actal_function(optimal_individual))
