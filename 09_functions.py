# Python Functions

# To define a function, write "def" followed by
# the name of the function.
# Inside the parentheses, list the inputs/arguments to the function
# (this is a require/non-default argument).
def f():
    pass # Tells Python to skip this line and do nothing.

# To call the function, type the name and parentheses.

# If you call the directory function dir(), f will be listed.

# Functions can return values.
def ping():
    return "Ping!"

print(ping())
x = ping()
print(x)

import math
def sphere_volume(r):
    """returns the volume of a sphere with radius r"""
    v = (4.0/3.0) * math.pi * r**3
    return v

print(sphere_volume(2))

def triangle_area(b, h):
    """returns the area of a triangle with base b and height h"""
    return 0.5 * b * h

print(triangle_area(3, 6))

# Functions can also accept keyword/default arguments.
# Must specify a value for a keyword argument by its name.
def cm(feet = 0, inches = 0):
    """converts a length from feet and inches to centimeters"""
    inches_to_cm = inches * 2.54
    feet_to_cm = feet * 12 * 2.54
    return inches_to_cm + feet_to_cm

# Keyword arguments help you write flexible functions.
print(cm(feet = 5))
print(cm(inches = 70))
print(cm(feet = 5, inches = 8))
print(cm(inches = 8, feet = 5))

# Can use both keyword arguments and required arguments,
# but the keyword arguments must come last.