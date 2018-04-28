#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 00:57:09 2018

@author: shubansa
Data Science Career Path Lesson 2
"""

"""
1. Matplotlib

"""
import matplotlib.pyplot as plt
plt.plot(x,y)
plt.show()

plt.scatter(x,y)
plt.xscale('log')
plt.show()

#Histograms

values = [0,0.4,4,5,2,4.5,6,7,2,1,0.6]
plt.hist(values, bins=3)
plt.show()

# Customizations

plt.xlabel('LabelForX')
plt.ylabel('LabelForY')
plt.title('TitleForPlot')
plt.yticks([0,2,6,8,10],
           ['0B','2B','6B','8B','10B'])

# To increase size of dots in scatter plot
# provide one more argument s which corresponds to size of dots
plt.scatter(x,y,s=sizeList)

# Add colors to the dots in scatter plot by
# providing one more c argument
plt.scatter(x,y, s=sizeList, c=colorList)

# to draw gridlines
plt.grid(True)


"""
2. Dictionaries

"""

names = {'Shubh':6,
         'Bansal':4,
         'Shubham':3
         }

# Print out keys of dictionary
print(names.keys())

# Simple print any value corresponsing to any key
print('Bansal' in names)

# to delete any key value
del(names['Shubh'])

# Dictionary of dictionaries
europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }


"""
3. Pandas

""""
import pandas as pd
# pandas dataframe is like a table
# rows represents observations
# columns represents variables
# different columns can have different types of values


# There are multiple ways to create Pandas Dataframes
# first from a dictionary
my_dict = {
    'country': ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt'],
    'drives_right': [True, False, False, False, True, True, True],
    'cars_per_cap': [809, 731, 588, 18, 200, 70, 45] 
}

cars = pd.DataFrame(my_dict)

row_labels = ['US', 'AUS', 'JAP', 'IN', 'RU', 'MOR', 'EG']

cars.index = row_labels

# second from a csv file
cars = pd.read_csv('cars.csv', index_col = 0)


# Now we will learn to select and index data from a pandas dataFrame
# if we only want to select column country from cars dataFrame
# this will return a pandas series
carsSeries = cars['country']

# this will return a pandas dataframe
carsDF = cars[['country']]


# if we want to select some rows from cars DataFrame
carsSelectedRows = cars[1:4]


# Now we select and index data using loc and iloc
print(cars.loc[['US','AUS','JP'],['country','drives_right']])

print(cars.iloc[[0,1,2],[0,1]])



"""
4. Operators and if-else
"""

#Boolean operators with numpy arrays
import numpy as np
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

# my_house greater than 18.5 or smaller than 10
print(np.logical_or(my_house>18.5,my_house<10))

# Both my_house and your_house smaller than 11
print(np.logical_and(my_house<11,your_house<11))



# Filtering pandas dataframes
medium = cars[np.logical_and(cars['cars_per_cap']>100, cars['cars_per_cap']<500)]


"""
5. Loops

"""

# For loops 
areas = [11.25, 18.0, 20.0, 10.75, 9.50]
for a in areas :
    print(a)

# Change for loop to use enumerate()
for i,a in enumerate(areas) :
    print("room "+str(i)+": "+str(a))


# Looping over data structures
# Looping over dictionaries used item method
europe = {'spain':'madrid', 'france':'paris', 'germany':'bonn', 
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'australia':'vienna' }
          
# Iterate over europe
for k,v in europe.items() :
    print("the capital of "+str(k) + " is " + str(v))
    

# Looping over numpy arrays use np.nditer() function
    
    
    

# Looping over pandas dataframe use iterrows method
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Iterate over rows of cars
for lab, val in cars.iterrows():
    print(lab)
    print(val)
    
    
    

"""
6. Random Numbers
"""

































