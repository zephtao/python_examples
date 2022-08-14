# Python and Prime Numbers

import math

# 1 is neither prime nor composite.

# Version 1: test all divisors from 2 through n-1 (skip 1 and n).
# Very slow for large ranges.
def is_prime_v1(n):
    """Return 'True' if 'n' is a prime number. False otherwise."""
    if n == 1:
        return False # 1 is not prime
    for d in range(2, n):
        if n % d == 0:
            return False
    return True

# Test version 1 on first 20 pos ints
for n in range(1, 21):
    print(n, is_prime_v1(n))

# Version 2: test all divisors from 2 through sqrt(n)
# Reduce number of divisors we check:
# Only have to test for integers up to sqrt(n),
# since the factors after that start to repeat.
# Much faster than Version 1.
def is_prime_v2(n):
    """Return 'True' if 'n' is a prime number. False otherwise."""
    if n == 1:
        return False # 1 is not prime
    max_divisor = math.floor(math.sqrt(n))
    for d in range(2, 1 + max_divisor):
        if n % d == 0:
            return False
    return True

# Test version 2:
for n in range(1, 21):
    print(n, is_prime_v2(n))

# Version 3:
# Step 1: test if n is even.
# Step 2: test only odd divisors.
# Twice as fast as Version 2.
def is_prime_v3(n):
    """Return 'True' if 'n' is a prime number. False otherwise."""
    if n == 1:
        return False # 1 is not prime
    # If n is even and not 2, then n is not prime.
    if n == 2:
        return True
    if n > 2 and n % 2 == 0:
        return False
    
    max_divisor = math.floor(math.sqrt(n))
    for d in range(3, 1 + max_divisor, 2): # step value of 2.
                                           # covers all odd numbers up to limit.
        if n % d == 0:
            return False
    return True

for n in range(1, 21):
    print(n, is_prime_v3(n))