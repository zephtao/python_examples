# CSV Files in Python

# Python has a CSV module.
# Comma Separated Values: format for storing data;
# text file that contains data.
# Everything in a CSV is represented as a string.
# Two commas in a row means that a piece of data is missing.

# https://goo.gl/3zaUlD
path = "/Users/ztao/Downloads/google_stock_market_data.csv"
file = open(path)
#for line in file:
#    print(line)

# Parse the data without using the CSV module.
# Read the contents using a list comprehension:
lines = [line for line in open(path)]
# Each line is treated as a single string.
print(lines[0])
# Remove leading or trailing white space:
print(lines[0].strip())
# Divide the string into smaller pieces:
print(lines[0].strip().split(','))

dataset = [line.strip().split(',') for line in open(path)]
print(dataset[0])

# Parse the data using the CSV module.
import csv
print(dir(csv))
file = open(path, newline='')
# Reader function to parse csv data from the file:
reader = csv.reader(file)

# The first line is the header, so use the next function
# to extract the first line:
header = next(reader)
# Read the remaining data:
data = [row for row in reader]
print(header)
print(data[0])

# Convert data to appropriate types:
from datetime import datetime
data = []
for row in reader:
    # row = [Date, Open, High, Low, Close, Volume, Adj. Close]
    # [datetime, float, float, float, float, integer, float]
    # Use string parse time:
    date = datetime.strptime(row[0], '%m/%d/%Y') # (string, expected format)
    open_price = float(row[1]) # 'open' is a built-in function
    high = float(row[2])
    low = float(row[3])
    close = float(row[4])
    volume = int(row[5])
    adj_close = float(row[6])

    data.append([date, open_price, high, low, close, volume, adj_close])

    print(data[0])

# Compute and store daily stock returns (% change in price):
returns_path = "/Users/ztao/Downloads/google_returns.csv"
file = open(returns_path, 'w') # write mode
# Create csv writer object for storing results:
writer = csv.writer(file)
writer.writerow(["Date", "Return"])

for i in range(len(data) - 1): # stops at second-to-last row
    todays_row = data[i]
    todays_date = todays_row[0]
    todays_price = todays_row[-1] # last element
    # the dates are in decreasing order
    yesterdays_row = data[i+1]
    yesterdays_price = yesterdays_row[-1]

    daily_return = (todays_price - yesterdays_price) / yesterdays_price
    writer.writerow([todays_date, daily_return])
    formatted_date = todays_date.strftime('%m/%d/%Y')
    writer.writerow([formatted_date, daily_return]) # INFO NOT TRANSFERRING TO CSV FILE??