# Datetime Module (Dates and Times)

# import the datetime module
import datetime

# three key classes in the datetime module: date, time, and datetime

# see what is inside the module by printing its directory
print(dir(datetime))

# To see help, call
# help(datetime.date)

# date(year, month, day) --> date object

my_birthday = datetime.date(2002, 6, 17)
print(my_birthday)

# timedelta object
mill = datetime.date(2000, 1, 1)
dt = datetime.timedelta(100)
print(mill + dt) # prints 2000-04-10

# To print dates in a diff format, you must
# create a format code. (>20 codes to choose from)
# Example:
# Day-name, Month-name, Day-#, Year
# older method:
print(my_birthday.strftime("%A, %B %d, %Y")) # Monday, June 17, 2002
# newer method:
message = "Zephyr was born on {:%A, %B %d, %Y}."
print(message.format(my_birthday))

# SpaceX rocket launch
launch_date = datetime.date(2017, 3, 30) # year, month, day
launch_time = datetime.time(22, 27, 0) # hours, minutes, seconds
launch_datetime = datetime.datetime(2017, 3, 30, 22, 27, 0) # year, month, day, hours, minutes, seconds
print(launch_date) # 2017-03-30
print(launch_time) # 22:27:00
print(launch_datetime) # 2017-03-30 22:27:00

# To access components of launch_time:
print(launch_time.hour) # 22
print(launch_time.minute) # 27
print(launch_time.second) #0

# To access components of launch_datetime:
print(launch_datetime.year)
print(launch_datetime.month)
print(launch_datetime.day)
print(launch_datetime.hour)
print(launch_datetime.minute)
print(launch_datetime.second)

# To get the current datetime in UTC format
now = datetime.datetime.today()
print(now) # stores time down to the microsecond
# can access the microsecond, too
print(now.microsecond)

# Convert strings to datetimes
moon_landing = "7/20/1969"
# method: strptime(), short for string parse time
# first argument: string containing the date
# second argument: expected format
moon_landing_datetime = datetime.datetime.strptime(moon_landing, "%m/%d/%Y")
print(moon_landing_datetime) # displays it in standard datetime format,
                             # which is an object, not a string
                             # an instance of the datetime class in the datetime module