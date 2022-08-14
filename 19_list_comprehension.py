# List Comprehension

# Let you construct a list in a single line of code.

# Surrounded by brackets, but instead of a list of data inside,
# you enter an expression followed by for loops and if clauses.

# Most basic form for a list comprehension:
# [expr for val in collection1 and collection2 and ...]
# expr: generates the elements in the list.
# for loop over some collection of data:
# evaluates the expression for every item in the collection.

# Only include the expression for certain pieces of data:
# [expr for val in collection if <test1> and <test2> and ...]

# Example: list of squares of the first 100 positive integers
# Without list comprehension:
squares = []
for i in range(1, 101):
    squares.append(i**2)
print(squares)

# With list comprehension:
squares2 = [i**2 for i in range(1, 101)]
print(squares2)

# Example: remainders when you divide the first 100 squares by 5
remainders5 = [x**2 % 5 for x in range(1, 101)]
print(remainders5)

remainders11 = [x**2 % 11 for x in range(1, 101)]
print(remainders11)

# Example: movies that start with "G"
movies = ["Star Wars", "Gandhi", "Toy Story", "Gone with the Wind", "The Wizard of Oz", "Gattaca",
          "Ghostbusters", "To Kill A Mockingbird", "Good Will Hunting", "Raiders of the Lost Ark",
          "Groundhog Day", "Close Encounters of the Third Kind"]
# Without list comprehension:
gmovies = []
for title in movies:
    if title.startswith("G"):
        gmovies.append(title)
print(gmovies)

# With list comprehension:
gmovies = [title for title in movies if title.startswith("G")]
print(gmovies)

# Example: movies released before 2000
movies = [("Citizen Kane", 1941), ("Spirited Away", 2001), ("Gattaca", 1997), ("No Country for Old Men", 2007),
           ("The Aviator", 2004), ("Raiders of the Lost Ark", 1981), ("Groundhog Day", 1993),
           ("Close Encounters of the Third Kind", 1977)]
pre2k = [title for (title, year) in movies if year < 2000]
print(pre2k)

# Example: scalar multiplication on vectors
v = [2, -3, 1]
# 4*v does not work: it simply concatenates the list 4 times.
# Use list comprehension:
w = [4*x for x in v]
print(w)

# Example: compute the Cartesian product of sets
# Cartesian product of sets A and B is the set of pairs (a, b)
# where 'a' is in A and 'b' is in B.
A = [1, 3, 5, 7]
B = [2, 4, 6, 8]
cartesian_product = [(a, b) for a in A for b in B]
print(cartesian_product)