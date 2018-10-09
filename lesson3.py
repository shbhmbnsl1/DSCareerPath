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

def shout() :
    print("Shout")

def shoutWithArg(word) :
    print(word + "Shout")
    return word

# tuples
nums = (2,4,6,8)



"""
2. Functions with multiple arguments and return values

"""

# functions can return multiple values in the form of tuples
# tuples will be used to return multiple values from a function
def multiReturn(num1, num2) :
    mul = num1*num2
    add = num1+num2
    sub = num1-num2
    numTuple = (mul, add, sub)
    return numTuple
mul, add, sub = multiReturn(5,3)
print(str(mul) + " " + str(add) + " " + str(sub))


"""
3. Functions with default arguments and variable length arguments

"""

# global keyword
g = 10
def myFun() :
    g = 2
    print(g)
    
def myFun2() :
    global g
    print(g)
    
myFun()
myFun2()


# function with variable length arguments. 
def funct(*args) :
    sum=0
    for i in args :
        sum = sum + i
        
    print(sum)

funct(1,2,3,1,2)
    

# function with variable length key value arguments.
def funct2(**kwargs) :
    for key,val in kwargs.items() :
        print(key + ":" + str(val))
        
funct2(name="Shubham", age=20, company="Amazon")


"""
4. Lambda functions

"""

# lambda functions are one line functions
my_fun = lambda x,y : x+y
res = my_fun(2,3)
res_str = my_fun("shubham","bansal")

# Using lambda functions with map
# map is used to apply a lambda function on some object example list
list1 = [2,4,6,8]
listAns = map(lambda x: x*2, list1)
listAns2 = list(listAns)
print(listAns2)


# Using lambda functions with filter
# filter applies some condition on a list
str_list = ["shubham","surbhi","vaibhav","bansal"]
str_filter_fun = filter(lambda mem: len(mem)>6,str_list)
str_f_list = list(str_filter_fun)


# Using lambda functions with reduce
# reduce is used to do some calculations on the list and it returns a single value
# in this case it returns all strings in the list concatenated to a single string
from functools import reduce
strReduceFun = reduce(lambda i1,i2: i1+i2, str_list)
print(strReduceFun)

        
        
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
        
        
        
        
        
        
        