import math
from random import randint, random

N = 8  # Size of the chessboard
max_iterations = 500  # Reduced maximum iterations to run the algorithm
initial_temperature = 1000  # Starting temperature
cooling_rate = 0.95  # Cooling rate for temperature decay
max_fitness = N * (N - 1) // 2  # Maximum fitness = total number of non-attacking pairs

# A utility function to configure the board with a random state
def configureRandomly(state):
    for i in range(N):
        state[i] = randint(0, N - 1)  # Place each queen randomly in a row

# A utility function to calculate the fitness (number of non-attacking pairs)
def calculateFitness(state):
    non_attacking_pairs = 0
    for i in range(N):
        for j in range(i + 1, N):
            if state[i] != state[j] and abs(state[i] - state[j]) != abs(i - j):
                non_attacking_pairs += 1
    return non_attacking_pairs

# A utility function to print the chessboard based on the current state
def printBoard(state):
    for i in range(N):
        row = ['.'] * N  # Initialize empty row
        row[state[i]] = 'Q'  # Place the queen
        print(' '.join(row))  # Print the row as a string
    print("\n")  # Add a newline after the board

# A utility function to get a neighbor state by moving a queen
def getNeighbor(state):
    new_state = state[:]
    row = randint(0, N - 1)
    new_row = randint(0, N - 1)
    new_state[row] = new_row  # Move the queen in the selected row to a new random row
    return new_state

# Simulated Annealing function
def simulatedAnnealing():
    state = [0] * N
    configureRandomly(state)
    current_fitness = calculateFitness(state)
    temperature = initial_temperature

    # Print the starting state
    print(f"Starting State: {state}, Fitness: {current_fitness}")
    printBoard(state)

    fitness_history = [current_fitness]  # To track fitness changes over time
    steps_taken = []  # List to store steps taken in this attempt

    for iteration in range(max_iterations):
        neighbor_state = getNeighbor(state)
        neighbor_fitness = calculateFitness(neighbor_state)

        fitness_difference = neighbor_fitness - current_fitness

        # Append current step number to the steps_taken list
        steps_taken.append(iteration + 1)

        # Accept the neighbor state based on the fitness difference and temperature
        if fitness_difference > 0:
            state = neighbor_state[:]
            current_fitness = neighbor_fitness
            print(f"Iteration {iteration + 1}: Moved to better state: {state}, Fitness: {current_fitness}")
            printBoard(state)  # Print the board after each move
        else:
            # Allow a "bad" move with a probability based on temperature
            acceptance_probability = math.exp(fitness_difference / temperature)
            if random() < acceptance_probability:
                state = neighbor_state[:]
                current_fitness = neighbor_fitness
                print(f"Iteration {iteration + 1}: Accepted worse state: {state}, Fitness: {current_fitness}")
                printBoard(state)  # Print the board after each move

        # Track fitness history
        fitness_history.append(current_fitness)

        # Cool down the temperature
        temperature *= cooling_rate

        if current_fitness == max_fitness:
            print(f"Solution found: {state}, Fitness: {current_fitness}")
            printBoard(state)
            return True, fitness_history, steps_taken  # Return steps taken as well

    print(f"Local Maximum reached, Final State: {state}, Fitness: {current_fitness}")
    printBoard(state)
    return False, fitness_history, steps_taken  # Return steps taken even if no solution is found

# Driver code to perform multiple random attempts
def multipleAttempts(num_attempts):
    solutions_found = 0
    total_steps_taken = 0  # Accumulate total steps taken across all attempts
    all_attempts_steps = []  # List to store steps taken for each attempt

    for attempt in range(1, num_attempts + 1):
        print(f"\nAttempt {attempt}:")
        solution_reached, fitness_history, steps_taken = simulatedAnnealing()  # Capture steps taken
        all_attempts_steps.append(steps_taken)  # Add steps taken in this attempt to the list
        total_steps_taken += len(steps_taken)  # Accumulate total steps

        if solution_reached:
            solutions_found += 1
            print("Reached a solution.")
        else:
            print("Did not reach a solution.")

        # Print the fitness change over time
        print("Fitness change over time:", fitness_history)
    
    # Print all attempts' steps together
    print("\nAll attempts' steps taken:", [len(steps) for steps in all_attempts_steps])
    # Print the total steps taken across all attempts
    print(f"Total steps taken across all {num_attempts} attempts: {total_steps_taken}")
    print(f"Total solutions found in {num_attempts} attempts: {solutions_found}")

if __name__ == "__main__":
    num_attempts = 100  # Set number of random attempts
    multipleAttempts(num_attempts)