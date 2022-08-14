# If, Then, Else in Python

# Example 1
# Collect string, then test its length.
# Can be used to validate new passwords.

# Uses the raw input function
# Prompts the user to enter a string,
# and stores the value in the variable "input".
input = input("Please enter a test string: ")

# The "if" line ends with a colon and
# the following lines are indented.
# This is how you identify a code block in Python:
# You start a new code block with a colon and
# group the commands with indentation.
if len(input) < 6:
    print("Your string is too short.")
    print("Please enter a string with at least 6 characters.")

# Example 2
# To test this part, comment out the above code.
# Prompt user to enter number - test if even or odd
input = input("Please enter an integer: ")
number = int(input)
if number % 2 == 0:
    print("Your number is even.")
else:
    print("You number is odd.")

# Example 3
# To test this part, comment out the above code.
# User enter lengths of the sides of a triangle.
# Tells whether it's scalene, isosceles, or equilateral.

a = int(input("The length of side a = "))
b = int(input("The length of side b = "))
c = int(input("The length of side c = "))

if(a != b and b != c and a != c):
    print("This is a scalene triangle.")
# elif means else if
elif a == b and b == c:
    print("This is an equilateral triangle.")
else:
    print("This is an isosceles triangle.")