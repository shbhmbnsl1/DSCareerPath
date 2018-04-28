#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 22:02:01 2018

@author: shubansa
Data Science career path Lesson 4
"""

"""
1. Iterators
"""

# Iterables and iterators 
list1 = [2,4,3,15,6,7]
it = iter(list1)
print(it.next())
print(it.next())
pritn(it.next())


# enumerate and zip functions
# enumerate() returns an enumerate object that 
# produces a sequence of tuples, and each of the tuples is an index-value pair
list2 = [3,6,8,4,2,9]
enum = enumerate(list2)
listOfEnum = list(enum)
for index,val in enum :
    print(index + ":" + val)

# by default index starts with 0 but we can change it by specifying additional start arg
enum2 = enumerate(list2, start=4)

# using zip function
list3 = [3,4,1,2,3]
zipList = list(zip(list1, list2, list3))
print(zipList)