# Urllib - GET Requests

# URL = Uniform Resource Locator
# https://en.wikipedia.org/wiki/URL?key=value&life=42#History

# Protocol/Scheme: http, https, ftp, ...
# Host: en.wikipedia.org
# Port (sometimes you will see a colon followed by a number): http=80, https=443
# Path: wiki/URL
# Querystring (text after the question mark): key=value&life=42
# ^ holds a collection of key-value pairs separated by &s (ampersands)
# Fragment (hashtag at the end followed by a string): History

# urllib: a package that simplifies the task of building, loading, and parsing URLs.
# Contains 5 modules:
# - request (open URLs)
# - response (used internally by the request module)
# - error (request exceptions; contains several error classes for use by the request module)
# - parse (useful URL functions; break up a URL into meaningful pieces)
# - robotparser (inspect robots.txt files for what permissions are granted to bots and crawlers)

# HTTP Status Codes
# 200: OK
# 400: bad request
# 403: forbidden
# 404: not found

import urllib
from urllib import request
# Just as open(file) opens files, urlopen(url) opens URLs.
resp = request.urlopen("https://www.wikipedia.org")
print(type(resp))
print(resp.code) # prints the response code 200, which is good.
print(resp.length) # size of the response in bytes.
print(resp.peek()) # look at a small part of the response

data = resp.read()
print(type(data))
print(len(data))
# decode the bytes object
html = data.decode("UTF-8")
print(type(html))
print(html)

# If you try to read the repsonse a second time (resp.read()), nothing happens.
# Once you read the response, Python closes the connection.

# https://www.youtube.com/watch?v=EuC-yVzHhMI&t=5m56s
# v = video ID, t = start time.
from urllib import parse
params = {"v": "EuC-yVzHhMI", "t": "5m56s"}
querystring = parse.urlencode(params)
print(querystring)
url = "https://www.youtube.com/watch" + "?" + querystring
resp = request.urlopen(url) # returns False - still have a connection with the server.
print(resp.isclosed())
html = resp.read().decode("utf-8")
print(html[:500]) # first 500 characters of the html