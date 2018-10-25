# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 13:01:18 2018

@author: shbhm
Data Science Career Path - Lesson 6
"""

"""
1. Importing files from the web
    1.1. Importing flat files from web, downloading them locally and reading directly
    1.2. Importing non flat files from the web

2. Making HTTP requests
    2.1. Using urllib package
    2.2. Using request package
    2.3. Scraping the web using BeautifulSoup

3. API's and JSON
    3.1. Loading and Exploring a JSON
    3.2. API Requests
    3.3. Using Twitter API
"""

"""
1.1. Importing flat files
"""
# Import necessary packages
# get the url of the file
# use urlretrieve function which is used to save the file locally. this uses two arguments
# arg1 is url and arg2 is file name
# then read the downloaded file to a pandas dataframe

# SAVE FILE LOCALLY FROM WEB
# Import package
from urllib.request import urlretrieve
import pandas as pd
url = 'https://s3.amazonaws.com/assets.datacamp.com/production/course_1606/datasets/winequality-red.csv'
# Save file locally.
urlretrieve(url, 'winequality-red.csv')
# Read file into a DataFrame and print its head
df = pd.read_csv('winequality-red.csv', sep=';')
print(df.head())


# DIRECTLY READING THE CONTENTS OF FILE FROM WEB
# we can directly read the contents of a file from the web without saving it locally
# directly pass the file url in pandas read_csv function
# Assign url of file: url
url = 'https://s3.amazonaws.com/assets.datacamp.com/production/course_1606/datasets/winequality-red.csv'
# Read file into a DataFrame: df
df = pd.read_csv(url, sep=';')
# Print the head of the DataFrame
print(df.head())



"""
1.2. Importing non flat files from the web
"""

# We can import non flat files like excel files from the web using pandas read_excel function
# the read_excel function will take two arguments
# arg1 is url of the file & arg2 is sheet_name which should be None if you want to select all sheets from file
# the output of pd.read_excel() is a Python dictionary with sheet names as keys and
# corresponding DataFrames as corresponding values.

# Import package
import pandas as pd
# Assign url of file: url
url = 'http://s3.amazonaws.com/assets.datacamp.com/course/importing_data_into_r/latitude.xls'
# Read in all sheets of Excel file: xl
xl = pd.read_excel(url, sheet_name=None)
# Print the sheetnames to the shell
print(xl.keys())
# Print the head of the first sheet (using its name, NOT its index)
print(xl['1700'].head())


"""
2.1. Making Http request using urllib function
"""

# Import urlopen and Request functions from urllib.request subpackage
# Package the request using Request function
# Send the request using urlopen function
# use the response for data example read the html content by using read method

# Import packages
from urllib.request import urlopen, Request
# Specify the url
url = "http://www.datacamp.com/teach/documentation"
# This packages the request: request
request = Request(url)
# Sends the request and catches the response: response
response = urlopen(request)
# Extract the response: html
html = response.read()
print(html)
# Be polite and close the response!
response.close()

"""
2.2. Making Http requests using requests package
"""
# Import package requests
# package the request, send the request and catch response using a single function call
# get the text attribute out from the response
# requests package provides a higher level interface with less code compared to urllib

# Import package
import requests
# Specify the url: url
url = 'http://www.datacamp.com/teach/documentation'
# Packages the request, send the request and catch the response: r
r = requests.get(url)
# Extract the response: text
text = r.text
# Print the html
print(text)


"""
2.3. Using BeautifulSoup
"""
# Beautiful Soup is a Python library for pulling data out of HTML and XML files
# Import package requests and function BeautifulSoup from package bs4
# Package and send the request and get response using get function from requests package
# Get html out of the response
# create a BeautifulSoup object using that html
# prettify the object

# Import packages
import requests
from bs4 import BeautifulSoup
# Specify url: url
url = 'https://www.python.org/~guido/'
# Package the request, send the request and catch the response: r
r = requests.get(url)
# Extracts the response as html: html_doc
html_doc = r.text
# Create a BeautifulSoup object from the HTML: soup
soup = BeautifulSoup(html_doc)
# Prettify the BeautifulSoup object: pretty_soup
pretty_soup = soup.prettify()
# Print the response
print(pretty_soup)
# Get title of webpage
print(soup.title)
# Get only the text of webpage
print(soup.get_text())
# Getting all the hyperlinks from the html content
a_tags = soup.find_all('a')
for link in a_tags:
    print(link.get('href'))


"""
3.1. Loading and Exploring a JSON
"""
# Import the package json
# open a json file using context with
# load the file's contents in a variable using json.load() function
# json.load function returns the json data as a python dictionary
# extract data from this dictionary

# import package json
import json
# Load JSON: json_data
with open("a_movie.json") as json_file:
    json_data = json.load(json_file)
# Print each key-value pair in json_data
for k in json_data.keys():
    print(k + ': ', json_data[k])


"""
3.2. API requests
"""
# Import requests package
# assign url with the required api endpoint
# Package and send the request and catch the response
# Print the text of the response
# we can also see the actual json by using json() method on the response object

# Import requests package
import requests
# Assign URL to variable: url
url = 'http://www.omdbapi.com/?apikey=ff21610b&t=the+social+network'
# Package the request, send the request and catch the response: r
r = requests.get(url)
# Print the text of the response
print(r.text)
# Decode the JSON data into a dictionary: json_data
json_data = r.json()
# Print each key-value pair in json_data
for k in json_data.keys():
    print(k + ': ', json_data[k])



"""
3.3. Using Twitter API
"""
# Import tweepy package which is used to handle all the Twitter API OAuth Authentication details
#

# Import package
import tweepy
# Store OAuth authentication credentials in relevant variables
access_token = "1092294848-aHN7DcRP9B4VMTQIhwqOYiB14YkW92fFO8k8EPy"
access_token_secret = "X4dHmhPfaksHcQ7SCbmZa2oYBBVSD2g8uIHXsp5CTaksx"
consumer_key = "nZ6EA0FxZ293SxGNg8g8aP0HM"
consumer_secret = "fJGEodwe3KiKUnsYJC3VRndj7jevVvXbK2D5EiJ2nehafRgA6i"
# Pass OAuth details to tweepy's OAuth handler
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
