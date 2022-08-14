# Python Random Number Generator: The Random Module

import random
print(dir(random))

# Random function: returns a random number
# in the interval 0 to 1: [0,1).
# Represents the uniform distribution.

# Display 10 random numbers from interval [0,1)
print("10 random numbers from interval [0,1):")
for i in range(10):
    print(random.random())

# Generate random numbers from interval [3,7).
# Method 1: write your own function.
def my_random():
    # Random, scale, shift, return.
    return 4 * random.random() + 3

print("10 random numbers from interval [3,7):")
for i in range(10):
    print(my_random())

# The random() function can be used to build
# customized random number generators.

# Method 2: use the 'uniform' function.
print("10 random numbers from interval [3,7):")
for i in range(10):
    print(random.uniform(3,7))

# random() and uniform() are both uniform distributions.

# To generate random numbers from a normal distribution,
# use normalvariate(u, o). u = mean, o = standard deviation.

# Mean = 0, SD = 1:
print("20 random numbers from a bell curve with mean 0 and SD 1:")
for i in range(20):
    print(random.normalvariate(0,1))

# Discrete Probability Distributions.
# Example: simulate the roll of a six-sided dice.
# Use randint(min, max).
print("20 rolls of a six-sided dice:")
for i in range(20):
    print(random.randint(1,6))

# Random element from a list.
# Example: rock, paper, scissors.
# Use choice().

# Define the list.
outcomes = ['rock', 'paper', 'scissors']

print("20 random choices between rock, paper, scissors:")
for i in range(20):
    print(random.choice(outcomes))