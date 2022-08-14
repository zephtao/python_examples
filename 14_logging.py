# Logging in Python

# Logging allows you to write status messages to a file
# or other output streams.

# These messages contain info on which parts of your code
# have executed and what problems may have arisen.

# Each log message has a level. The five built-in levels are
# Debug, Info, Warning, Error, Critical.

# Constants
# Level     Numeric Value
# NOTSET    0
# DEBUG     10
# INFO      20
# WARNING   30
# ERROR     40
# CRITICAL  50

import logging
import math

print(dir(logging))
# Entries in all caps are constants.
# Capitalized items are classes.
# Items that start with lowercase letter are methods.

# Create and configure logger
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename = "E:\\python\\Lumberjack.Log",
                    level = logging.DEBUG, format = LOG_FORMAT)
# If you want the second message to override the first, add
# filemode = 'w' as an argument above.

# Create logger object
logger = logging.getLogger()

# Test the logger
logger.info("Our first message.")

print(logger.level)

# By default, the log file is written in append mode.

# You can log messages of any level by calling the method with the level name.

# Test messages
logger.debug("This is just a harmless debug message.")
logger.info("Just some useful info.")
logger.warning("I'm sorry, but I can't do that.")
logger.error("Did you just try to divide by zero?")
logger.critical("The entire internet is down!")
# If you change the log level in line 30 to any of these,
# only the message for that level and above will be displayed.

# Quadratic Formula example
def quadratic_formula(a, b, c):
    """Return the solutions to the standard quadratic equation"""
    logger.info("quadratic_formula({0}, {1}, {2})".format(a, b, c))

    # Compute the discriminant
    logger.debug("# Compute the discriminant")
    disc = b**2 - 4*a*c

    # Compute the two roots
    logger.debug("# Compute the two roots")
    root1 = (-b + math.sqrt(disc)) / (2*a)
    root2 = (-b - math.sqrt(disc)) / (2*a)

    # Return the roots
    logger.debug("# Return the roots")
    return (root1, root2)

roots = quadratic_formula(1, 0, -4)
print(roots)