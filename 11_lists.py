# Python Lists

# lists make it easy to work with ordered data
# lists preserve the order of the data

# two ways to create a list
# Method 1: use the list constructor
example = list()

# Method 2 (simpler and more common):
# use brackets
example = []

# Can pre-populate a list with values
primes = [2, 3, 5, 7, 11, 13]
# Add to a list
primes.append(17)
primes.append(19)

# display the list
print(primes)

# can access a specific value by its index
# index starts with 0
print(primes[0])
# If you go below 0, Python wraps back around
# to the end of the list.
# The last item is -1, the next to last is -2, ...
# Convenient when you want to look at the last values.
print(primes[-1])
# Can only wrap around once (in primes, no further than -8).

# Slicing lets you retrieve a range of values from the list
# given a start and end index.
# Includes the start index value, excludes the end index value.
print(primes[2:5])

# Lists in Python can contain values of different types.
example = [128, True, "Alpha", 1.732, [64, False]]
# Lists can contain duplicate values.

# Can combine lists (concatenation).
numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
print(numbers + letters)

# To see all methods for lists, pass any list
# to the directory function.
print(dir(numbers))