# Python Booleans

# Boolean values: True, False
# Take note that the T and F are capitalized

a = 3
b = 5
print(a == b) # False
print(a != b) # True
# can also test a > b, a < b

# type(True) is 'bool'
# type(False) is 'bool'

# Another way to create booleans is by passing values
# to the boolean constructor.

# In Python, 0 is converted to False, while
# every other number is converted to true.
bool(28) # returns True
bool(-2.71828) # returns True
bool(0) # returns False

# In Python, the empty string is converted to False, while
# every other string is converted to True.
bool("Turing") # returns True
bool(" ") # returns True
bool("") # returns False

# This holds in general for boolean conversions:
# trivial values -> False
# non-trivial values -> True

# Just as you can convert objects to booleans,
# you can convert booleans to other types of objects.

str(True) # returns 'True'
str(False) # returns 'False'

int(True) # returns 1
int(False) # returns 0

5 + True # is 6
10 * False # is 0