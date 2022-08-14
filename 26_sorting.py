# Sorting in Python

# Sorting alphabetically:
earth_metals = ["Beryllium", "Magnesium", "Calcium", "Strontium", "Barium", "Radium"]
alphabetical = earth_metals.sort()
print(earth_metals)
reverse_alphabetical = earth_metals.sort(reverse=True)
print(earth_metals)

earth_metals_tuple = ("Beryllium", "Magnesium", "Calcium", "Strontium", "Barium", "Radium")
# No sort method for tuples, since tuples are immutable objects.
# Planets currently sorted by distance from Sun.
# format := (name, radius, density, distance from Sun)
planets = [
    ("Mercury", 2440, 5.43, 0.395),
    ("Venus", 6052, 5.24, 0.723),
    ("Earth", 6378, 5.52, 1.000),
    ("Mars", 3396, 3.93, 1.530),
    ("Jupiter", 71492, 1.33, 5.210),
    ("Saturn", 60268, 0.69, 9.551),
    ("Uranus", 25559, 1.27, 19.213),
    ("Neptune", 24764, 1.64, 30.070)
]
# Sort the planets by size, largest to smallest.
size = lambda planet: planet[1]
planets.sort(key=size, reverse=True)
print(planets)

# Sort by density, least to most.
density = lambda planet: planet[2]
planets.sort(key=density)
print(planets)

# list.sort() changes the list.
# Create a sorted copy?
# Sort a tuple?
# Use sorted()
# help(sorted)
# sorted(iterable, /, *, key=None, reverse=False)
earth_metals = ["Beryllium", "Magnesium", "Calcium", "Strontium", "Barium", "Radium"]
sorted_earth_metals = sorted(earth_metals)
print(sorted_earth_metals) # sorted
print(earth_metals) # unchanged

# Sort a tuple:
data = (7, 2, 5, 6, 1, 3, 9, 10, 4, 8)
print(sorted(data))
print(data)

# Returns a list of all the characters in the string, sorted alphabetically.
print(sorted("Alphabetical"))