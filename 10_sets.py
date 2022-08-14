# Sets in Python

# sets don't store duplicates.
# order doesn't matter in a set.

# empty set
example = set()

# to see a list of methods you can use on a set,
# use the directory function on the set.
print(dir(example))

# help(example.add)

# You can add data of different types
# to the same set.
example.add(42)
example.add(False)
example.add(3.14159)
example.add("Thorium")

print(example)

# to see how many elements are in a set
print(len(example))

# remove an element
example.remove(42)
print(example)
# remove(): KeyError if you try to remove an element
# that's not in the set.

# discard(): does nothing if you try to remove an element
# that's not in the set. Removes an element if it is.

# Can pre-populate a set with a collection of elements.
example2 = set([28, True, 2.71828, "Helium"])
print(len(example2))

# Empties out the set and removes all elements.
example2.clear()
print(len(example2))

# Union of sets A and B is the combination
# of all elements from the two sets.

# Intersection is the set of elements
# inside both A and B.

# Integers 1-10
odds = set([1, 3, 5, 7, 9])
evens = set([2, 4, 6, 8, 10])
primes = set([2, 3, 5, 7])
composites = set([4, 6, 8, 9, 10])

# all the integers from 1-10
print(odds.union(evens))
print(evens.union(odds))

# odd prime numbers
print(odds.intersection(primes))

# even prime numbers
print(primes.intersection(evens))

# no integers are even and odd
print(evens.intersection(odds))

# To see if an element is (or is not) in a set,
# use the "in" operator.
print(2 in primes)
print(6 in odds)