# Interactive Help

# dir()
# Short for "directory".
# When you press enter, Python displays a list of available objects.
# When you first start the interpreter, there are four standard objects:
# [ '__builtins__', '__doc__', '__name__', '__package__'].

# builtins: a module that contains a collection of common objects
# which are always available.
# To see the list of builtin objects, call the directory function
# and pass it the builtins module name: dir(__builtins__)
# The list contains dozens of functions and types ready for use.

# To learn about one of these objects, call the help function
# with the name of the object.

# Example: help(pow) will display the help documentation
# for the pow function.
# pow(...)
    # pow(x, y[, z]) -> number
    # With two arguments, equivalent to x**y. With three arguments,
    # equivalent to (x**y) % z, but may be more efficient (e.g. for longs).

print(pow(2, 10)) # = 2^10 = 1024
print(2**10) # = 2^10 = 1024

# help(hex)
    # hex(number) -> string
    # Return the hexadecimal representation of an integer or long integer.

print(hex(10)) # = '0xa'
# the hexadecimal representation of 10 is 'a'
# hexadecimals in Python begin with '0x'

# To convert a hexidecimal back to a regular decimal,
# type in the hex value without quotation marks.
print(0xa) # prints 10

# Think of a module as a folder that contains other Python objects.
# To see a list of available modules, call help('modules')

# To learn about a module and see what objects are available,
# you must first import it.
import math
print(dir()) # the math module should appear
print(dir(math))
# To view the help for a function, you must specify
# the path to the function.
# help(math.radians)

rad = math.radians(180) # = pi = 3.14159 radians
print(rad)

# There is a way to import a function so that you
# do not have to type the full path (saves time).
# Will be discussed in a later video on importing modules.