# Text Files in Python

# Two kinds of files:
# Text files: human-readable data (e.g. plain text, XML, JSON, source code)
# Binary files: store compiled code, app data, and media files (images, audio, video)

# To open a file, use the built-in "open" function.
# guido_bio.txt is in the "text_files" folder of python_examples.

# One way to open a file:
f = open("text_files/guido_bio.txt")
text = f.read()
f.close()
print(text)

# Open a file using the "with" keyword (better and safer):
# You do not need to close the file, that is done for you.
# Python will close the file even if an exception occurs in the code block.
with open("text_files/guido_bio.txt") as fobj:
    bio = fobj.read()

print(bio)

# To handle a FileNotFoundError:
try:
    with open("text_files/future_lottery_numbers.txt") as f:
        text = f.read()
except FileNotFoundError:
    text = None
print(text)

# Write to a text file:
oceans = ["Pacific", "Atlantic", "Indian", "Southern", "Arctic"]
with open("text_files/oceans.txt", "w") as f:
    for ocean in oceans:
        f.write(ocean)
        f.write("\n")

# Another way to ensure each element is on a separate line:
# with open("text_files/oceans.txt", "w") as f:
#   for ocean in oceans:
#       print(ocean, file=f)

# Opening in write mode ("w") overwrites existing contents of the file.
# Opening in append mode ("a") writes to a file without overwriting any existing text.
with open("text_files/oceans.txt", "a") as f:
    print(23*"=", file=f)
    print("These are the 5 oceans.", file=f)

# Print the contents of "oceans.txt"
with open("text_files/oceans.txt") as fobj:
    theOceans = fobj.read()

print(theOceans)