#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 16:22:50 2018

@author: shubansa
Data Science Carrer Path Lesson 3
"""


"""
1. Writing own functions
"""




"""
2. Functions with multiple arguments and return values

"""

# functions can return multiple values in the form of tuples



"""
3. Functions with default arguments and variable length arguments

"""

def funct(*args) :
    sum=0
    for i in args :
        sum = sum + i
        
    print(sum)

funct(1,2,3,1,2)
    

def funct2(**kwargs) :
    for key,val in kwargs.items() :
        print(key+" " + val)
        

funct2(name="Shubham", age=20)


"""
4. Lambda functions

"""

my_fun = lambda x,y : x+y
res = my_fun(2,3)

# Using lambda functions with map
list1 = [2,4,6,8]
listAns = map(lambda x: x*2, list1)
listAns2 = list(listAns)
        
        
"""
5. Error Handling
"""

def sqrt(x) :
    try:
        return x**0.5
    except :
        print('x must be an int or float')
        
# Catch only specific type of errors
def sqrt(x):
    try:
        return x**0.5
    except TypeError :
        print('x must be an int or float')
        
        
def sqrt(x):
    if x<0 :
        raise ValueError('x can"t be negative')
    try:
        return x**0.5
    except TypeError :
        print('x must be an int or float')
        
        
        
        
        
        
        
        