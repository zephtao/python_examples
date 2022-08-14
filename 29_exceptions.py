# Exceptions in Python

# Exception: an object with a description of what went wrong,
# and a traceback of where the problem occurred.

# Common exceptions:
# SyntaxError
# ZeroDivisionError
# FileNotFoundError
# TypeError
# ValueError

# General way to handle exceptions:
try:
    # runs first
except:
    # runs if exception occurs in try block
else:
    # executes if try block succeeds (skips except block)
finally:
    # always executes, regardless of what happens above