# Artificial_Intelligence_Algorithms
**Hill Climbing vs Simulated Annealing**``

**Hill Climbing Algorithm.**
Valid Solutions:
Hill Climbing Algorithm works on random generation of a grid so for each time
num of actual solutions may vary depending upon the condition of a grid .For
example this algo found 85 correct solutions at the end (it may vary for the next
one) .
Total number of steps:
As we know we have to run this code for 100 attempts then for each attempt num
of steps to find a solution will be different therefore I print them as:
But again point to consider is that it may vary for each execution of code due to
random grid generation .
Time and Memory / Space complexity.
• Worst case time consumption is about O(n ^ m) where n is the number of
states in the search space, and m is the maximum depth of the search space.
• Average case time complexity is O(n).
• Best case time complexity is O(1) that is constant
• Worst case memory or space complexity ( consumption) is O(n) when the
algorithm has to take track of current , neighbor and previously explored
states.
• Best Case space complexity is about O(1)
Advantages:
• It is easier to implement.
• It is the greedy approach so we have to check local best one so it is easier.
• It consumes low memory.
Disadvantages:
• It always goes for local maxima not for global maxima.
• It cannot find the exact solution on flat surfaces
• It does not keep track of previously explored states ( that is known as back
tracking)
• It mostly depends upon the starting point

**Simulated Annealing Algorithm:**
Valid Solutions:
Simulated Annealing Algorithm works on random generation of a grid so for each
time num of actual solutions may vary depending upon the condition of a grid .For
example this algo found 34 correct solutions at the end (it may vary for the next
one) .
Total number of steps:
As we know we have to run this code for 100 attempts then for each attempt num
of steps to find a solution will be different therefore I print them as:
Time and Space Complexity:
• In worst case the theoretical time consumption tends to infinity mean unable
to calculate but mathematically and logically we bound it to O(N ^ 2)
• In average case it is about nlogn or it may be n^2 because it depends upon
number of iterations and number of solutions explored or checked.
• In best case scenario its time complexity is about O(n)
• Its worst case space complexity is O(n)
• It s best case space complexity is O(1)
Advantages:
• It can find the global maxima as in the above mentioned problem it can
reach to a solution only when max fitness is about 28
• It is suitable for large search spaces due to probability based working.
• We can choose the cooling factor according to specific problems
• It does backtracking
Disadvantages:
• There is no surety of reaching the solution.
• It is strongly dependent on parameters like cooling factors , number of
iterations , stopping factor etc.
• the cooling schedule and neighborhood structure can introduce complexity
in implementation so we can say that it is complex than Hill Climbing
algorithm


**Genetic Algorithm vs Hill Climbing and Annealing**
Valid Solutions:
Genetic Algorithm works on random generation of a grid so for each time num of
actual solutions may vary depending upon the condition of a grid .For example this
algo found 35 correct solutions at the end (it may vary for the next one) .
Time and Memory / Space Complexity:
• However, Time complexity for 8-queen problem via Genetic Algorithm
depends upon several other factors like fitness evaluation , selection , cross
over and mutation.
• The best or optimal case is when actual solution( that is 28 in this problem)
found in early generations.
• Thus fitness evaluation time complexity is O(N^2).
• For selection it is O(P)
• For cross over it is O(N)
• For mutation it is O(1)
• Thus overall is : O(Gb⋅(P⋅N^2))=O(Gb⋅P⋅N^2) where Gb is small (that is
number of generations )because the solution is found early.
• In average case fitness evaluation time complexity is O(N^2).
• For selection it is O(P)
• For cross over it is O(N)
• For mutation it is O(1)
• Thus overall complexity in average case is: O(Ga⋅(P⋅N^2))=O(Ga⋅P⋅N^2)
• For worst case fitness evaluation time complexity is O(N^2).
• For selection it is O(P)
• For cross over it is O(N)
• For mutation it is O(1)
• Thus overall time complexity is: O(Gmax⋅(P⋅N^2))=O(Gmax⋅P⋅N^2)
• In all cases, the space required to store the population is O(P⋅N) where P is
the population size and N is the number of queens.
Advantages:
• It has capability to find the global optimal solution just like as Annealing
algorithm whereas Hill Climbing algorithm does not has this capability to
find global maximum.
• It allows parallel exploration of various solutions on basis of genetic
population while annealing and hill climbing algos work on single solution
base approach.
• Large population and capability of mutation allows this algorithm to do the
global search in a better way as compare to annealing algorithm while other
one can find local minima only.
• Due to large population it will provide more reliable solution as compare to
those algorithms.
Disadvantages:
• It consumes too much time because of large genetic population and it
includes various computationally expensive steps like fitness evaluation ,
mutation etc.
• The performance of a GA is highly sensitive to parameters such as
population size, mutation rate, crossover rate, and the number of
generations.
• High reliance on randomness can cause large deviation among results for
every execution of algorithm.
• There is no surety of optimal solution at the end in highly complex search
spaces.
