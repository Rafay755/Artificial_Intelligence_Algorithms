from random import randint

N = 8  # You can change this for different sizes of the chessboard
max_sideways_moves = 100  # Limit for sideways moves
max_restarts = 100  # Random restarts count
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

# A utility function to get the best neighbor state
def getBestNeighbor(state):
    best_state = state[:]
    best_fitness = calculateFitness(state)

    for i in range(N):
        for j in range(N):
            if j != state[i]:
                new_state = state[:]
                new_state[i] = j  # Move the queen in the ith column to row j
                new_fitness = calculateFitness(new_state)
                if new_fitness > best_fitness:
                    best_state = new_state[:]
                    best_fitness = new_fitness
                elif new_fitness == best_fitness:  # Allow sideways move
                    if randint(0, 1):  # Randomly choose to accept or not
                        best_state = new_state[:]
    
    return best_state, best_fitness

# Hill climbing function with sideways moves
def hillClimbingWithSidewaysMoves():
    state = [0] * N
    configureRandomly(state)
    current_fitness = calculateFitness(state)
    sideways_moves = 0
    steps = 0  # Initialize steps taken in this attempt

    print(f"Starting State: {state}, Fitness: {current_fitness}")
    printBoard(state)  # Print the initial board

    while sideways_moves < max_sideways_moves:
        neighbor_state, neighbor_fitness = getBestNeighbor(state)

        steps += 1  # Increment the steps counter

        if neighbor_fitness > current_fitness:
            state = neighbor_state[:]
            current_fitness = neighbor_fitness
            print(f"Moved to better state: {state}, Fitness: {current_fitness}")
            printBoard(state)  # Print the board after each move
        elif neighbor_fitness == current_fitness:
            state = neighbor_state[:]
            sideways_moves += 1
            print(f"Sideways move: {state}, Fitness: {current_fitness}, Sideways count: {sideways_moves}")
            printBoard(state)  # Print the board after a sideways move
        else:
            break

        if current_fitness == max_fitness:
            print(f"Solution found: {state}, Fitness: {current_fitness}")
            printBoard(state)  # Print the final solution board
            return True, steps  # Return steps taken

    print(f"Local Maximum reached, Fitness: {current_fitness}")
    printBoard(state)  # Print the local maximum board
    return False, steps  # Return steps taken even if no solution is found

# Main function to perform random restarts
def randomRestartHillClimbing():
    solutions_found = 0
    total_steps = 0  # Variable to accumulate total steps taken across all attempts
    steps_list = []  # List to collect steps taken in each attempt

    for attempt in range(1, max_restarts + 1):
        print(f"\nAttempt {attempt}:")
        solution_reached, steps = hillClimbingWithSidewaysMoves()  # Capture steps taken
        total_steps += steps  # Accumulate total steps
        steps_list.append(steps)  # Add steps to the list

        if solution_reached:
            solutions_found += 1
            print("Reached a solution.")
        else:
            print("Did not reach a solution.")

    # Print the collected steps for all attempts
    print(f"\nSteps taken in each attempt: {{{', '.join(map(str, steps_list))}}}")
    print(f"Total solutions found in {max_restarts} attempts: {solutions_found}")
    print(f"Total steps taken across all attempts: {total_steps}")  # Print total steps taken

# Driver code
if __name__ == "__main__":
    randomRestartHillClimbing()