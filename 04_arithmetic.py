# Arithmetic in Python Version 3

# operations: +, -, *, /

# any int can be represented by a float, but not the other way around

x = 28 # int
print(x)
# to convert an int to a float, just add a .0 at the end
x = 28.0 # float
print(x)
# another way is to pass an int to the float constructor
print(float(28))
# not all floats can be converted to ints
# ints are narrower than floats
# floats are wider than ints

# any float can be made into a complex number, but not vice versa
x = 1.732 # float
print(x)
# to convert a float to a complex number, just add 0j to the number
x = 1.732 + 0j
print(x)
# or pass the number to the complex constructor
print(complex(1.732))
# floats are narrower than complex numbers
# complex numbers are wider than floats

# Arithmetic Operations

a = 2 # int
b = 6.0 # float
c = 12 + 0j # complex number

# when combining two numbers of diff types, Python will convert the
# narrower type to the wider type, then perform the operation

# addition
print(a + b) # int + float
# Python converts "a" to a float, then adds it to "b"
# 2.0 + 6.0 = 8.0

# subtraction
print(b - a) # float - int
# Python widens "a" to a float, then subtracts it from "b"
# 6.0 - 2.0 = 4.0

# multiplication
print(a * 7) # int * int
# no widening required
# 2 * 7 = 14

# division
print(c / b) # complex / float
# "b" is widened to a complex number before the division
# (12 + 0j / 6 + 0j) = (2 + 0j)

# In Python Version 3, if you divide two whole numbers,
# the result is a float (even if there is no remainder).
print(16/5) # = 3.2

# percent operator: returns the remainder
print(16 % 5) # = 1

# double division symbol: returns the quotient
print(16 // 5) # = 3

# cannot divide by 0 - throws error