import random


items = {
    'A': {'weight': 2, 'value': 3},
    'B': {'weight': 3, 'value': 5},
    'C': {'weight': 4, 'value': 7},
    'D': {'weight': 5, 'value': 9}
}
int_pop = [
    [1, 1, 1, 1],
    [1, 0, 0, 0],
    [1, 0, 1, 0],
    [1, 0, 0, 1]
]

psize = 4
max_capacity = 9
order  = ['C', 'A', 'D', 'B']




def fitness(x):
    total_weight = sum(items[item]['weight'] for item, bit in zip(items.keys(), x) if bit == 1)
    if total_weight > max_capacity:
        return 0
    total_value = sum(items[item]['value'] for item, bit in zip(items.keys(), x) if bit == 1)
    return total_value

def crossover(p1, p2):
    crossover_point = len(p1) // 2
    child1 = p1[:crossover_point] + p2[crossover_point:]
    child2 = p2[:crossover_point] + p1[crossover_point:]
    return child1, child2


def mutation(offspring):
    mutation_bit_index = order .pop(0)
    index = list(items.keys()).index(mutation_bit_index)
    offspring[index] = 1 - offspring[index]  # Flip the bit
    order .append(mutation_bit_index)
    return offspring
 
def selection(population):
    sorted_population = sorted(population, key=lambda x: fitness(x), reverse=True)
    return sorted_population[:2]








def genetic_algorithm(int_pop, iterations):
    population = int_pop.copy()

    for i in range(iterations):
        fittest = selection(population)
        offspring1, offspring2 = crossover(population[2], population[3])
        offspring1 = mutation(offspring1)

        population = fittest + [offspring1, offspring2]

    return population

# Run the genetic algorithm for 4 iterations
result_population = genetic_algorithm(int_pop, 4)

# Output the result
print("Result after 4 iterations:")
for x in result_population:
    print(x, "Fitness:", fitness(x))
