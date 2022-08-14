# JSON in Python

# JavaScript Object Notation
# A small, lightweight data format.
# A packet of JSON data is almost identical to a Python dictionary.
# Shorter than XML, and can be quickly parsed by browsers since it
# uses JavaScript syntax.
# Ideal format for transporting data between a client and a server.

# true and false are not capitalized.
# instead of "none," use "null."

# All the keys are strings.
# The values can be strings, numbers, booleans, list, null, or even another JSON object.

# Use the JSON Module in Python
import json
# print(dir(json))
# json.load(f): load JSON data from file (or file-like object)
# json.loads(s): load JSON data from a string
# json.dump(j, f): write JSON object to file (or file-like object)
# json.dumps(j): output JSON object as string

# json.load example:
json_file = open("movie_1.txt", "r")
movie = json.load(json_file)
json_file.close()
print(movie)

print(type(movie)) # class 'dict'
print(movie["title"])
print(movie["actors"])

# json.loads example:
# Use if your JSON data arrives in the form of a string.
# Common in client-server applications where data is sent over the net.
# Shift + Enter does something in the terminal!!!
value = """ {"title": "Tron: Legacy", "composer": "Daft Punk", "release_year": 2010, "budget": 170000000, "actors": null, "won_oscar": false} """
tron = json.loads(value)
print(tron)

# Suppose you want to store the data about Gattaca in a database or send it to a remote user.
# To convert this dictionary into a valid JSON string, use the json.dumps() method.
# json.dumps example:
dumps = json.dumps(movie)
print(dumps)

# To allow unicode (non-ASCII) characters in your string,
json.dumps(movie, ensure_ascii=False)

# json.dump example:
movie2 = {}
movie2["title"] = "Minority Report"
movie2["director"] = "Steven Spielberg"
movie2["composer"] = "John Williams"
movie2["actors"] = ["Tom Cruise", "Colin Farrell", "Samantha Morton", "Max von Sydow"]
movie2["is_awesome"] = True
movie2["budget"] = 102000000
movie2["cinematographer"] = "Janusz Kaminski"
file2 = open("/Users/ztao/Desktop/movie_2.txt", "w")
json.dump(movie2, file2)
file2.close()