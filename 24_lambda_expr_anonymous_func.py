# Lambda Expressions & Anonymous Functions

# Lambda expressions = anonymous functions.
# Functions that have no name.
# Cannot use lambda expressions for multi-line functions.

# Write function to compute 3x+1:
def f(x):
    return 3*x + 1
print(f(2))

# Keyword lambda --> inputs --> colon --> expression that is the return value.
lambda x: 3*x + 1

# One way to use it is to give the function a name:
g = lambda x: 3*x + 1
print(g(2))

# Lambda expression with multiple inputs:
# Want to combine first and last name into a single full name.
full_name = lambda fn, ln: fn.strip().title() + " " + ln.strip().title()
print(full_name("    leonhard", "EULER"))

# A function with no name:
# Want to sort authors by last name.
scifi_authors = ["Isaac Asimov", "Ray Bradbury", "Robert Heinlein", "Arthus C. Clarke", "Frank Herbert", "Orson Scott Card", "Douglas Adams", "H.G. Wells", "Leigh Brackett"]
# Create an anonymous function that extracts the last name and uses it as the sorting value.
# The key argument is a function that will be used for sorting. We will pass it a lambda expression.
# To access the last name, split the string into pieces wherever it has a space.
# Next, access the last piece by index -1, and convert to lowercase as a precaution.
scifi_authors.sort(key=lambda name: name.split(" ")[-1].lower())
print(scifi_authors)

# A function that builds functions:
def build_quadratic_function(a, b, c):
    """Returns the function f(x) = ax^2 + bx + c"""
    return lambda x: a*x**2 + b*x + c

# 2x^2 + 3x - 5:
f = build_quadratic_function(2, 3, -5)
print(f(0))
print(f(1))
print(f(2))

# 3x^2 + 1. Passes in the value x = 2.
print(build_quadratic_function(3, 0, 1)(2))