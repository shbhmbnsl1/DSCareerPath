#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 22:02:01 2018

@author: shubansa
Data Science career path Lesson 4 (Python Data Science ToolBox Part 2)
"""

"""
1. Iterators 
    1.1 Iterables and iterators
    1.2 ** Enumerate function **
    1.3 ** Zip function **
    1.4 Iterators Use Case
"""

# 1.1 Iterables and iterators 
# iterable is any ds which can be iterated over e.g. list, dictionary, files etc.
# iterator is an object which is used to iterate over any iterable
list1 = [2,4,3,15,6,7]
it = iter(list1)
print(next(it))
print(next(it))
print(next(it))



# 1.2 ENUMERATE function
# used to add counter to any iterable
# @param any iterable object as an argument
# @return enumerate object 
# this enumerate object contains the elements of the original iterable and their index within the iterable 
# as tuples. we can change the start index by specifying start=# default is 0
avengers = ['iron man','spider man','thor','captain america']
e = enumerate(avengers)
print(list(e))
# UNPACKING ENUMERATE object
for index, value in e:
    print(index, value)

e2 = enumerate(avengers, start = 10)    



# 1.3 ZIP function 
# used to stich together an arbitary number of iterables
# @param arbitary number of iterables 
# @return an iterator of tuples
# this iterator of tuples will have elements from each iterable
name = ['Elon','Jeff','Mukesh','Shubham']
surname = ['Musk','Bezos','Ambani','Bansal']
age = [45, 43, 54, 21]
z = zip(name, surname, age)
print(type(z))
#print(list(z))
# UNPACKING ZIP object
for n1,n2,n3 in z:
    print(n1,n2,n3)

# For UNZIPPING we can use *
z = zip(name,surname,age)
n1, n2, n3 = zip(*z)
print(n1)
print(n2)
print(n3)


# 1.4 ITERATORS - USE CASE
# used to load large files which are so large that it is not possible to load in memory at once
# load those files in chunks using pandas read_csv function
# the object created by read_csv is an iterable which can be iterated over to do calculations
import pandas as pd
result = []
for chunk in pd.read_csv('shubham.csv', chunksize = 20):
    result.append(sum(chunk['x']))
total = sum(result)



"""
2. List Comprehensions and generators
    2.1 List Comprehensions
    2.2 Advanced Comprehensions
    2.3 Dictionary Comprehensions
    2.4 Generator Expressions
    2.5 Generator Functions

"""

# 2.1 LIST COMPREHENSIONS
# used to generate list from any iterable
# in only one line of code.
# list comprehensions can be used with any iterable
# how? 
# Collapse for loops for building lists into a single line
# Required components: 1. Iterable 2. Iterator 3. Output expression
list1 = [1,2,3,4,5]
newList = [num+1 for num in list1]
otherList = [num for num in range(10)]
# List comprehensions can also be used like this
# this will generate [(0,6),(0,7),(1,6),(1,7)]
pairList = [(num1,num2) for num1 in range(0,2) for num2 in range(6,8)]
# Example 2 : Create a 5X5 matrix 
matrix = [[col for col in range(5)] for row in range(5)]
print(matrix)


# 2.2 ADVANCED COMPREHENSIONS
# Conditionals on the iterable
adList = [num**2 for num in range(10) if num%2 == 0]
# Conditionals on the output expression
adList2 = [num**2 if num%2==0 else 0 for num in range(10)]


# 2.3 DICTIONARY COMPREHENSIONS
# two differences between list comprehensions and dictionary comprehensions
# first is curly brackets are used
# second is key value pairs are specified with colon in the output expression
positiveNegative = {num: -num for num in range(10)}
print(positiveNegative)



# 2.4 GENERATOR EXPRESSIONS
# used similar to list comprehensions
# will not create a list and instead it will create a generator object
# it is not storing list in memory but the object can be iterated over 
# this is useful when we are working with very large lists that cant be stored in memory
# all the things possible on list comprehensions are also possible on generator expressions
generator = (num for num in range(10))
print(list(generator))
# we can also print by passing iterator function next on the generator object
print(next(generator))
print(next(generator))
unexp = [num for num in range(10**10000)]
print(unexp)

# 2.5 GENERATOR FUNCTIONS
# Generator function when called produce generator objects
# they will return generator object but we do not use return 
# yield is used to return values from the function which are stored inside a generator object automatically
# that generator object is returned ultimately when function is called
def seqNums(n):
    i = 0
    while i<n:
        yield i
        i+=1
        
result = seqNums(5)
print(type(result))
print(list(result))








