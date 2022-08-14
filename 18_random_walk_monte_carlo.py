# A Random Walk & Monte Carlo Simulation

# You live in a city where the streets are arranged in a perfect grid.
# At each intersection, you choose your next direction randomly.
# Choices: N, S, E, W. (Backtracking permitted).
# If you are > 4 blocks away from home when you're done,
# you will pay for a transport back home.
# Otherwise, you will walk home.

# What is the longest random walk you can take so that on average,
# you will end up 4 blocks or fewer from home?

# Write random walk situation.
# Version 1: Simple.
import random
def random_walk(n):
    """Return coordinates after 'n' block random walk."""
    x = 0
    y = 0
    for i in range(n):
        # Use the chocie function to pick a random step:
        step = random.choice(['N', 'S', 'E', 'W'])
        if step == 'N':
            y = y + 1
        elif step == 'S':
            y = y - 1
        elif step == 'E':
            x = x + 1
        else:
            x = x - 1
    return (x, y)

# Test version 1:
# Take 25 random walks, each 10 blocks long.
print("Testing version 1:")
for i in range(25):
    walk = random_walk(10)
    # Display coordinates and distance from home.
    # Distance = sum of abs values of x- and y- coordinates.
    print(walk, "Distance from home = ",
         abs(walk[0]) + abs(walk[1]))

# Version 2: Short (using Python shortcuts).
def random_walk_2(n):
    """Return coordinates after 'n' block random walk."""
    x, y = 0, 0
    for i in range(n):
        (dx, dy) = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        x += dx
        y += dy
    return (x, y)

# Test version 2:
print("Testing version 2:")
for i in range(25):
    walk = random_walk_2(10)
    print(walk, "Distance from home = ",
         abs(walk[0]) + abs(walk[1]))

# Monte Carlo is a gambling town on the Mediterranean Sea.
number_of_walks = 10000
for walk_length in range(1, 31):
    no_transport = 0 # Number of walks 4 or fewer blocks from home.
    for i in range(number_of_walks):
        (x, y) = random_walk_2(walk_length)
        distance = abs(x) + abs(y)
        if distance <= 4:
            no_transport += 1
    no_transport_percentage = float(no_transport) / number_of_walks
    print("Walk size = ", walk_length, " / % of no transport = ", 100*no_transport_percentage)

# Run:
# The longest walk with a > 50% chance of walking home is a walk of size 22 blocks.
# In general, even walks end closer to home than odd walks.