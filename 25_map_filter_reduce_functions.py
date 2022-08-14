# Map, Filter, and Reduce Functions

import math

def area(r):
    """Area of a circle with radius 'r'."""
    return math.pi * (r**2)

# What if we need to compute the areas for many different circles?
radii = [2, 5, 7.1, 0.3, 10]

# Method 1: direct method
areas = []
for r in radii:
    a = area(r)
    areas.append(a)

print(areas)

# Method 2: use 'map' function
# Takes two arguments: (1) function, (2) list, tuple, or other iterable object.
map(area, radii)
# The output is a map object, not a list. This is highly favorable, esp with large collections of data.
# Returns an iterator over the function applied to each piece of data in the iterable object.
# Can turn it into a list by passing the map to the list constructor.
area_map = list(map(area, radii))
print(area_map)

# Convert temp from Celsius to Fahrenheit:
temps = [("Berlin", 29), ("Cairo", 36), ("Buenos Aires", 19), ("Los Angeles", 26), ("Tokyo", 27),
         ("New York", 28), ("London", 22), ("Beijing", 32)]
# Accept a tuple as input, return a tuple with the same name, but the temp in F:
c_to_f = lambda data: (data[0], (9/5)*data[1] + 32)
temp_in_f = list(map(c_to_f, temps))
print(temp_in_f)

# 'filter' function
# Select certain pieces of data from a list, tuple, or other collection of data.
# Filter out all values above the average:
import statistics
data = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]
avg = statistics.mean(data)
print("Average before filter: ", avg)
# First argument is a function, second is the list:
filter(lambda x: x > avg, data)
# Returns the data for which the function is true.
# Return value is a filter object, which is an iterator over the results.
results_list = list(filter(lambda x: x > avg, data))
print(results_list)

# Remove missing data:
countries = ["", "Argentina", "", "Brazil", "Chile", "", "Colombia", "", "Ecuador", "", "", "Venezuala"]
# Filters out values that are treated as false, including the empty string.
countries_list = list(filter(None, countries))
print(countries_list)

# reduce function (functools module)
# 99% of the time an explicit for loop is more readable.
from functools import reduce
# Multiply all numbers in a list using reduce function:
data = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
multiplier = lambda x, y: x*y
print(reduce(multiplier, data))
# Using a for loop:
product = 1
for x in data:
    product = product * x
print(product)