import random

# Number of queens (8-Queens)
N = 8

# Fitness function: counts how many pairs of queens are not attacking each other
def fitness(chromosome):
    non_attacking_pairs = 0
    for i in range(N):
        for j in range(i + 1, N):
            if chromosome[i] != chromosome[j] and abs(chromosome[i] - chromosome[j]) != abs(i - j):
                non_attacking_pairs += 1
    return non_attacking_pairs

# Print the board based on the current state
def printBoard(state):
    for i in range(N):
        row = ['.'] * N  # Initialize empty row
        row[state[i]] = 'Q'  # Place the queen
        print(' '.join(row))  # Print the row as a string
    print("\n")  # Add a newline after the board

# Generates a random chromosome (random positions of queens)
def create_chromosome():
    return [random.randint(0, N - 1) for _ in range(N)]

# Selects a parent using roulette wheel selection
def select_parent(population):
    fitness_scores = [fitness(chrom) for chrom in population]
    total_fitness = sum(fitness_scores)
    probabilities = [f / total_fitness for f in fitness_scores]
    return population[random.choices(range(len(population)), probabilities)[0]]

# Crossover (single-point crossover)
def crossover(parent1, parent2):
    crossover_point = random.randint(0, N - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

# Mutation: randomly change the row of one queen
def mutate(chromosome):
    i = random.randint(0, N - 1)
    chromosome[i] = random.randint(0, N - 1)
    return chromosome

# Genetic Algorithm
def genetic_algorithm():
    # Initialize population
    population_size = 100
    generations = 100
    mutation_rate = 0.1
    restarts = 100
    solutions_found = 0
    
    for restart in range(restarts):
        print(f"Restart #{restart + 1}")
        population = [create_chromosome() for _ in range(population_size)]
        print("Initial state:")
        printBoard(population[0])
        
        for generation in range(generations):
            population = sorted(population, key=lambda chrom: -fitness(chrom))
            current_best = population[0]
            current_fitness = fitness(current_best)
            print(f"Generation {generation + 1}, Fitness: {current_fitness}")
            printBoard(current_best)
            
            if current_fitness == 28:
                print(f"Solution found in generation {generation + 1}:")
                printBoard(current_best)
                solutions_found += 1
                break
            
            # Create new population with elitism
            new_population = population[:2]  # Elitism: carry over the best 2 chromosomes
            
            while len(new_population) < population_size:
                parent1 = select_parent(population)
                parent2 = select_parent(population)
                child1, child2 = crossover(parent1, parent2)
                if random.random() < mutation_rate:
                    child1 = mutate(child1)
                if random.random() < mutation_rate:
                    child2 = mutate(child2)
                new_population += [child1, child2]
            
            population = new_population
        
        if fitness(population[0]) != 28:
            print("No solution found in this restart.\n")
    
    print(f"\nTotal solutions found: {solutions_found} out of {restarts}")

# Run the algorithm
genetic_algorithm()