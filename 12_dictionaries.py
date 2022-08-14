# Python Dictionaries

# dictionaries are the same as maps in Java

# To create a dictionary:

# Method 1:
# Between curly braces, list the key name, a colon, and the value.
# If there's more than one key-value pair, separate them using a comma.
# Can use different data types for keys and values - mix and match.
# type(dictionary) will reveal that dictionary is an instance of the 'dict' class.
post = {"user_id":209, "message":"D5 E5 C5 C4 G4", "language":"English",
"datetime":"20230215T124231Z", "location":(44.590533, -104.715556)}
print(post)

# Method 2:
# Use the 'dict' constructor.
post2 = dict(message="SS Cotopaxi", language="English")
print(post2)

# Add data by using brackets.
# Key name (must be surrounded by quotes) goes inside [].
# Use = to assign the value.
post2["user_id"] = 209
post2["datetime"] = "19771116T093001Z"

print(post2)

# Accessing data
print(post['message'])

# To check if a key is in a dictionary:
if 'location' in post2:
    print(post2['location'])
else:
    print("The post does not contain a location value.")
# or:
try:
    print(post2['location'])
except KeyError:
    print("The post does not have a location.")

# Another way to access data:

# First, display the directory for the dictionary
print(dir(post2))
# help(post2.get)
loc = post2.get('location', None)
print(loc)

# Iterate over all the key-value pairs
# Method 1:
for key in post.keys():
    value = post[key]
    print(key, "=", value)
# Method 2:
for key, value in post.items():
    print(key, "=", value)
print(dir(post))
# The pop and popitem methods allow you to remove a single item.
# The clear method removes all data.