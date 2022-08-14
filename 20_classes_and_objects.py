# Python Classes and Objects

# Define a class by writing the "classs" keyword,
# followed by the name of the class, then a colon.

class User:
    pass # pass is a way to type a line that does nothing.

user1 = User() # user1 is an instance of User / an object.
user1.first_name = "Dave"
user1.last_name = "Bowman" # first_name and last_name are fields (data attached to an object).
# field names should be in lowercase, with words separated by underscores.

print(user1.first_name)
print(user1.last_name)

# standalone variables
first_name = "Arthur"
last_name = "Clarke"
print(first_name, last_name)

print(user1.first_name, user1.last_name)

user2 = User()
user2.first_name = "Frank"
user2.last_name = "Poole"

user1.age = 37
user2.favorite_book = "2001: A Space Odyssey"

import datetime

class User:
    """A member of FriendFace. Stores their name and birthday."""

    # init method : initialization/constructor
    def __init__(self, full_name, birthday):
        self.name = full_name
        self.birthday = birthday # right: value provided when you create a user object.
                                 # left: field that stores the value.
                                 # yyyymmdd
        # Extract first and last names
        name_pieces = full_name.split(" ")
        self.first_name = name_pieces[0]
        self.last_name = name_pieces[-1]
    
    def age(self):
        """Return the age of the user in years."""
        today = datetime.date(2001, 5, 12)
        # Convert birthday string into date object
        yyyy = int(self.birthday[0:4])
        mm = int(self.birthday[4:6])
        dd = int(self.birthday[6:8])
        dob = datetime.date(yyyy, mm, dd) # date object
        age_in_days = (today - dob).days
        age_in_years = age_in_days / 365
        return int(age_in_years)

user = User("Dave Bowman", "19710315")
print(user.name)
print(user.birthday)
print(user.age())