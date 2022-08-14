# Python Tuples

# Smaller, faster alternative to lists.

# List: data surrounded by brackets.
# Tuple: data surrounded by parentheses.

# In both:
# - can use the length function.
# - can iterate over the sequence.

# print(dir(list))
# Lists have more methods than tuples, but
# lists occupy more memory than tuples.
# print(dir(tuple))

import sys
print(dir(sys))
# print(help(sys.getsizeof))
# ^ tells you the size of an object in bytes.
# For a list and tuple holding the same elements,
# the list will take more bytes.

# You can add, remove, and change data in lists.
# Tuples cannot be changed - they are immutable.
# Tuples can be made more quickly than lists.

import timeit
list_test = timeit.timeit(stmt="[1, 2, 3, 4, 5]", number=1000000)
tuple_test = timeit.timeit(stmt="(1, 2, 3, 4, 5)", number=1000000)
print("List time: ", list_test)
print("Tuple time: ", tuple_test)

empty_tuple = ()
# looks like a string, because that's what it is
test1 = ("a")
# tuple containing a single element (has a comma after)
test1 = ("a",)

# can also make tuples without the parentheses
test1 = 1,
test2 = 1, 2

# tuple assignment:
# (age, country, knows_python)
survey = (27, "Vietnam", True)

age = survey[0]
country = survey[1]
knows_python = survey[2]

print("Age = ", age)
print("Country = ", country)
print("Knows Python? ", knows_python)

# alternative way to assign:
survey2 = (21, "Switzerland", False)
age, country, knows_python = survey2

print("Age = ", age)
print("Country = ", country)
print("Knows Python? ", knows_python)