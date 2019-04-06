POPULATION_SIZE = 500
INDIVIDUALS_FROM_TOURNAMENT = 10
TOURNAMENT_SIZE = 20
NUMBER_OF_POINTS = 200
NUMBER_OF_GENERATIONS = 5

import random

from Function import Function


def print_population(population):
    for function in reversed(population):
        print(str(function.coefficients) + " Fitness score: " + str(function.fitness_score))


def elitism(population, population_copy):
    population_copy.sort(key=lambda fn: fn.fitness_score, reverse=True)
    for fun in population_copy[:int(POPULATION_SIZE/10)]:
        population.append(fun)


def tournament_selection(population, iterations):
    temp_population = []
    elitism(temp_population, population)
    for i in range(iterations):
        tournament_population = random.sample(population, int(POPULATION_SIZE/iterations))
        tournament_population.sort(key=lambda fn: fn.fitness_score, reverse=True)

        for individual in tournament_population[:int(INDIVIDUALS_FROM_TOURNAMENT / iterations)]:
            temp_population.append(individual)

    return temp_population[:POPULATION_SIZE]


def crossover_coefficients(first_coefficient, second_coefficient):
    if first_coefficient > 0:
        first_parent_coefficient_binary = bin(first_coefficient)[2:]
    else:
        first_parent_coefficient_binary = bin(first_coefficient)[3:]
        first_parent_coefficient_binary = '-' + first_parent_coefficient_binary

    if second_coefficient > 0:
        second_parent_coefficient_binary = bin(second_coefficient)[2:]
    else:
        second_parent_coefficient_binary = bin(second_coefficient)[3:]
        second_parent_coefficient_binary = '-' + second_parent_coefficient_binary

    if len(first_parent_coefficient_binary) <= len(second_parent_coefficient_binary):
        len_ = len(first_parent_coefficient_binary)
        child_coefficient_binary = list(second_parent_coefficient_binary)
    else:
        len_ = len(second_parent_coefficient_binary)
        child_coefficient_binary = list(first_parent_coefficient_binary)

    pivot_val = random.randint(0, 100)
    if pivot_val > 90:
        return random.randint(-500, 500)

    for i in range(len_):
        if pivot_val < 40:
            child_coefficient_binary[i] = first_parent_coefficient_binary[i]
        elif pivot_val < 80:
            child_coefficient_binary[i] = second_parent_coefficient_binary[i]
        else:
            child_coefficient_binary[i] = str(random.randint(0, 1))

    if len(child_coefficient_binary) and child_coefficient_binary[0] != '-':
        return int(''.join(child_coefficient_binary), 2)
    return 0


def crossover_helper(first_parent, second_parent):
    child = Function()
    child.coefficients.clear()

    for i in range(len(first_parent.coefficients)):
        child.coefficients.append(crossover_coefficients(first_parent.coefficients[i], second_parent.coefficients[i]))

    return child


def crossover(population):
    # print("Population size: " + str(len(population)))
    temp_population = []
    for _ in range(POPULATION_SIZE):
        parent1 = random.choice(population)
        parent2 = random.choice(population)
        temp_population.append(crossover_helper(parent1, parent2))

    return temp_population


def calculate_population_fitness(population, points):
    for function in population:
        function.calculate_fitness(points)


def algorithm(functions, points):
    fitness_list = []
    population = functions
    for function in population:
        function.calculate_fitness(points)

    population.sort(key=lambda f: f.fitness_score, reverse=True)

    for _ in range(NUMBER_OF_GENERATIONS):
        print_population(population)
        population = tournament_selection(population, 10)
        population = crossover(population)
        calculate_population_fitness(population, points)

        population.sort(key=lambda f: f.fitness_score, reverse=True)
        fitness_list.append(population[0].fitness_score)

    return population[0], fitness_list
