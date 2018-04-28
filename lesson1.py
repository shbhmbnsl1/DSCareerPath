#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 03:33:09 2018

@author: shubansa
Data Science Career Path Lesson 1 
"""



"""
1. Python Lists

"""
a = []

# to delete element from list
del(a[0])

# to subset lists
x = a[1:6]

# to make copy of list 
c = list(a)




"""
2. Python Functions and methods

"""

# String methods
string = "shubham"
string_upper = string.upper()

# List methods
list1 = [1,2,3,4]
print(list1.index(2))
list1.append(5)
list1.reverse()


"""
3. Python Packages

"""

# NumPy package -- for arrays
import numpy as np
list2 = [1,4,3,7]
arr = np.array(list2)

# to subset numpy arrays based on some condition
# this line will make an array from arr with only elements greater than 3
arr2 = arr[arr>3]

# calculations can be done over entire array in one go
arr3 = arr*5

# Subsetting numpy arrays is same as python lists
arr4 = arr[2:4]

# 2D numpy arrays
list3 = [[2,3,4],
         [4,5,2],
         [7,4,8]]

arrr = np.array(list3)
print(arrr.shape)  # prints 3,3 because 3X3 matrix

# Subsetting 2D numpy arrays is very easy
x = [["a", "b"], ["c", "d"]]
[x[0][0], x[1][0]]

import numpy as np
np_x = np.array(x)
np_x[:,0] # indices before comma represent rows and after comma represent columns

# Statistics using numpy arrays
import numpy as np
x = [1, 4, 8, 10, 12]
np.mean(x)
np.median(x)

