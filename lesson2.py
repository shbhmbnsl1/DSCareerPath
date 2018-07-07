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
# this is normal line plot
plt.plot(x,y)
plt.show()

# scatter plot is just the plotting of data points without any line connecting those points
plt.scatter(x,y)
plt.xscale('log')
plt.show()

#Histograms
# histograms A histogram is an accurate representation of the distribution of numerical data
# It is an estimate of the probability distribution of a continuous variable 
# in simple words it plots count of number of values within a given range
# histogram is plotted for only one list unlike scatter and plot
values = [0,0.4,4,5,2,4.5,6,7,2,1,0.6]

# by default the bin size is 10
plt.hist(values, bins=3)
plt.show()

# to clean up the plot
plt.clf()

# Customizations

plt.xlabel('LabelForX')
plt.ylabel('LabelForY')
plt.title('TitleForPlot')
plt.yticks([0,2,6,8,10],
           ['0B','2B','6B','8B','10B'])

# To increase size of dots in scatter plot
# provide one more argument s which corresponds to size of dots
sizeList = np.array([3,5,2,7])
plt.scatter(x,y,s=sizeList)

# Add colors to the dots in scatter plot by
# providing one more c argument
plt.scatter(x,y, s=sizeList, c=colorList)

# adding text to some cooordinates
plt.text(1550, 71, 'India')
plt.text(5700, 80, 'China')

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

# This checks whether 'Bansal' is a key or not in names dict. Prints out true or false
print('Bansal' in names)

# to delete any key value
del(names['Shubh'])

# Dictionary of dictionaries
europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }

# To print capital of germany we write
print(europe['germany']['capital'])


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
# The keys become column names and the list of values become the whole columns

my_dict = {
    'country': ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt'],
    'drives_right': [True, False, False, False, True, True, True],
    'cars_per_cap': [809, 731, 588, 18, 200, 70, 45] 
}

cars = pd.DataFrame(my_dict)
print(cars)
# Printing cars looks like this
"""
        cars_per_cap        country  drives_right
    0           809  United States          True
    1           731      Australia         False
    2           588          Japan         False
    3            18          India         False
    4           200         Russia          True
    5            70        Morocco          True
    6            45          Egypt          True
"""
# Row labels are automatically set from 0 to 6

row_labels = ['US', 'AUS', 'JAP', 'IN', 'RU', 'MOR', 'EG']
cars.index = row_labels
# Now instead of 0 to 6 these keywords will be assigned to each row

# second from a csv file
# index_col is an optional arg
# if we do not specify it, we will get an additional column with indexes 0
# if we specify it, then indexes for rows would be the column number specified
cars = pd.read_csv('cars.csv', index_col = 0)


# Now we will learn to select and index data from a pandas dataFrame
# if we only want to select column country from cars dataFrame
# this will return a pandas series
carsSeries = cars['country']

# this will return a pandas dataframe
carsDF = cars[['country']]

# Select dataFrame with multiple columns
print(cars['country','cars_per_cap'])

# we can use square brackets to select rows as well
# if we want to select some rows from cars DataFrame
carsSelectedRows = cars[1:4]


# Now we select and index data using loc and iloc
# loc is label based
# iloc is integer index based

# printout single row
print(cars.loc['JAP'])

# use double square brackets to get as a pandas DataFrame
print(cars.loc[['JAP','AUS']])

# loc and iloc allows to select both rows and columns
print(cars.loc['JAP', 'drives_right'])
print(cars.iloc[4,0])

# first [] is list of rows to be selected, second [] is list of columns to be selected
print(cars.loc[['JAP','US'],'drives_right'])
print(cars.loc[['US','AUS','JP'],['country','drives_right']])
print(cars.iloc[[0,1,2],[0,1]])
print(cars.iloc[2:4,1:4])

# to select only columns using loc and iloc
print(cars.loc[:, 'drives_right'])
print(cars.loc[:, ['country','drives_right']])


# if we only need to select the rows for which drives_right is true
print(cars[cars['drives_right']])
# cars['drives_right'] selects the drives_right column 



"""
4. Operators and if-else
"""

#Boolean operators with numpy arrays
import numpy as np
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

# operational operators like < , > work normally with numpy arrays 
# but to use boolean operators special methods are used.
 

# my_house greater than 18.5 or smaller than 10
# will return a list of booleans corresponding to the condition specified
print(np.logical_or(my_house>18.5,my_house<10))
# this will print [False  True False  True]

# Both my_house and your_house smaller than 11
print(np.logical_and(my_house<11,your_house<11))
# this will print [False False False  True]





# Filtering pandas dataframes
# in this this example the main [] has a logical_and condition
# this logical_and statement will return a list of boolean values which corresponds to the condition
# inside the method. all rows which have cars_per_cap > 100 and < 500 will be returned.
medium = cars[np.logical_and(cars['cars_per_cap']>100, cars['cars_per_cap']<500)]


"""
5. Loops

"""

# While loop
offset = 10
while offset>0 :
    print(offset)
    offset = offset - 1

# For loops 
areas = [11.25, 18.0, 20.0, 10.75, 9.50]
for a in areas :
    print(a)

# Change for loop to use enumerate()
# using enumerate we can get both index and value from the list
for i,a in enumerate(areas) :
    print("room "+str(i)+": "+str(a))
    

# nested loops
house = [["hallway", 11.25], 
         ["kitchen", 18.0], 
         ["living room", 20.0], 
         ["bedroom", 10.75], 
         ["bathroom", 9.50]]
for r in house:
    for n in r:
        print(n)



# Looping over data structures
# Looping over dictionaries is done using item method
europe = {'spain':'madrid', 'france':'paris', 'germany':'bonn', 
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'australia':'vienna' }
# Iterate over europe
for k,v in europe.items() :
    print("the capital of "+str(k) + " is " + str(v))
    

# Looping over numpy arrays 
# for looping over 1D numpy arrays it is simple
nums = [1,4,3,7]
arrNums = np.array(nums)
for n in arrNums:
    print(str(n))

# for looping over 2D numpy arrays use numpy.nditer(arrayName) method
nums2D = [[2,3,4],
         [4,5,2],
         [7,4,8]]

arrNums2D = np.array(nums2D)
for val in np.nditer(arrNums2D):
    print(str(val))
    
    

# Looping over pandas dataframe use iterrows method
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)
# Iterate over rows of cars
for lab, val in cars.iterrows():
    print(lab)
    print(val)
# this will print each row as a Pandas series
# this prints each row with its label 
# we can print only some columns from the DataFrame
    print(str(lab) + " : " + str(val['cars_per_cap']))
    
    
# Add new column to DataFrame
# if we want to add a new column to the DataFrame we can do so using for loop and iterrows() and loc
for lab, val in cars.iterrows():
    cars.loc[lab, "country_len"] = len(row['country'])

# but this approach is not very efficient because 
# DataFrame can be huge and looping over each row is not efficient
# So if we want to add a column which is obtained by calling a function on another existing column 
# to a DataFrame then we can use apply method
# example below adds COUNTRY column which is uppercase version of country column
cars["COUNTRY"] = cars["country"].apply(str.upper)
    

"""
6. Random Numbers
"""

# Random numbers can be generated using seed() and rand() function
# seed(): sets the random seed, so that your results are the reproducible between simulations
# rand(): if you don't specify any arguments, it generates a random float between zero and one

import numpy as np
np.random.seed(123)
print(np.random.rand())
print(np.random.randint(1,7))

