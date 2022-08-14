# Recursion, the Fibonacci Sequence, and Memoization

# Fibonacci Sequence: 1, 1, 2, 3, 5, 8, 13, 21
# First two terms are 1, subsequent terms are the
# sum of the previous two terms.

# Write function to return the nth term of the Fib Seq.

# A very slow function (useless beyond a few dozen terms):
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)

for n in range(1, 11): # first 10 terms
    print(n, ":", fibonacci(n))

# Memoization: store the values for recent function calls
# so that future calls don't have to repeat the work.
# In other words, cache values.

# Implement explicitly:
fibonacci_cache = {} # dictionary
def fibonacci(n):
    # If we have cached the value, then return it.
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    # Compute the nth term
    if n == 1 or n == 2:
        value = 1
    elif n > 2:
        value = fibonacci(n-1) + fibonacci(n-2)
    # Cache the value and return it
    fibonacci_cache[n] = value
    return value

for n in range(1, 101): # first 100 terms
    print(n, ":", fibonacci(n))

# Built-in Python tool:
from functools import lru_cache # Least Recently Used Cache:
                                # provides a one-line way to add
                                # memoization to functions
# In parentheses, enter the number of values to cache.
# Default: 128 most recent values.
@lru_cache(maxsize = 1000)
# Define original slow function (with additional valid argument check):
def fibonacci(n):
    # Check that the input is a positive integer.
    if type(n) != int:
        raise TypeError("n must be a positive integer")
    if n < 1:
        raise ValueError("n must be a positive integer")
    # Compute the nth term.
    if n == 1 or n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)

for n in range(1, 501): # first 500 terms
    print(n, ":", fibonacci(n))

for n in range(1, 51): # first 50 terms
    # Ratio between consecutive terms
    print(fibonacci(n+1) / fibonacci(n))
    # The ratio converges to the Golden Ratio