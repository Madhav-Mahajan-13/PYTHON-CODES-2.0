import random


items = {
    'A': {'weight': 45, 'value': 3},
    'B': {'weight': 40, 'value': 5},
    'C': {'weight': 50, 'value': 8},
    'D': {'weight': 90, 'value': 10}
}

int_pop = [
    [1, 1, 1, 1],
    [1, 0, 0, 0],
    [1, 0, 1, 0],
    [1, 0, 0, 1]
]

psize = 4
max_capacity = 100
order_bit = ['D', 'C', 'B', 'A']






def selection(population):
    sorted_population = sorted(population, key=lambda x: fitness(x), reverse=True)
    return sorted_population[:2]  # first 2 ke liye

def fitness(x): #x --chromosoes
    total_weight = sum(items[item]['weight'] for item, bit in zip(items.keys(), x) if bit == 1)
    if total_weight > max_capacity:
        return 0
    total_value = sum(items[item]['value'] for item, bit in zip(items.keys(), x) if bit == 1)
    return total_value



def mutation(y): #y -- offspringss

    mutation_bit_index = order_bit.pop(0)
    index = list(items.keys()).index(mutation_bit_index)
    y[index] = 1 - y[index]  # Flip the bit
    order_bit.append(mutation_bit_index)
    return y

def crossover(parent1, parent2):
    mid = len(parent1) // 2
    child1 = parent1[:mid] + parent2[mid:]
    child2 = parent2[:mid] + parent1[mid:]
    return child1, child2




def genetic_algorithm(int_pop, iterations):
    population = int_pop.copy()

    for i in range(iterations):
        fittest = selection(population)
        y1, y2 = crossover(population[2], population[3])
        y1 = mutation(y1)

        population = fittest + [y1, y2]

    return population


result_population = genetic_algorithm(int_pop, 10)


print("10 iterations:")
for x in result_population:
    print(x, "Fitness:", fitness(x))

# print(fitness[0])