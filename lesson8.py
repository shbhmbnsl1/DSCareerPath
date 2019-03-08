#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 00:24:40 2018

@author: shubansa
Data Science Career Path - Lesson 8 Pandas Foundation
"""

"""
1. Data ingestion and inspection
    1.1. Reviewing pandas data frames
    1.2. Building dataframes from scratch
    1.3. Importing and exporting data
    1.4. Plotting with pandas
    
2. Exploratory data analysis
    2.1. Visual exploratory data analysis
    2.2. Statistical exploratory data analysis

3. Time series in pandas
    3.1. Indexing time series in pandas
    3.2. Resampling pandas time series
    3.3. Manipulating pandas time series
    3.4. Visualizing pandas time series

"""

"""
1.1. Reviewing pandas data frames
"""

df.info()
df.head()
# Numpy and pandas work together closely
# Create array of DataFrame values: np_vals
np_vals = df.values
# Create new array of base 10 logarithm values: np_vals_log10
np_vals_log10 = np.log10(np_vals)
# Create array of new DataFrame by passing df to np.log10(): df_log10
df_log10 = np.log10(df)


"""
1.2. Building dataframes from scratch
"""

# in this module we will build dataframe from a number of lists 
# suppose we have three lists: name, sex, age
import pandas as pd
name = ['Dwayne', 'Gigi', 'Drake', 'Rihanna']
age = [30, 26, 32, 35]
sex = ['M', 'F', 'M', 'F']
# we will create a list of keys which will represent the column names for the dataframe
list_keys = ['names', 'age', 'sex']
# below list is a list of lists of values 
list_values = [name, age, sex]
# zip both lists together into tuple form, this will return a zip type object
zipped = zip(list_keys, list_values)
print(zipped)


# convert zip object into list
list_zip = list(zipped)
print(list_zip)
# convert above list into dictionary
dictionary = dict(list_zip)
# convert dictionary into dataframe
dataframe = pd.DataFrame(dictionary)
print(dataframe)


"""
1.3. Importing and exporting data
"""

# Importing data from csv files is very convenient with pandas read_csv function
# read csv file into a dataframe using read_csv function
df = pd.read_csv(any_file_name)
# the read_csv function will by default consider first line of file as headers 
# if we want to change column headers for dataframe we can use additional arguments as below
df2 = pd.read_csv('any_file_name.csv', header = 0, names = ['column_name_1', 'column_name_2', 'column_name_3'])
# many more arguments are present for read_csv function
# read more on https://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html


"""
1.4. Plotting with pandas
"""

# Plotting series using pandas .plot() method
# Suppose we have dataframe df 
# the plot method automatically place index values on the x-axis
import matplotlib.pyplot as plt
df = pd.DataFrame({'Temperature': [79.0, 78.9, 76.5, 77.7]})
df.plot(color='red')
# Add a title
plt.title('Temperature in Austin')
# Specify the x-axis label
plt.xlabel('Hours since midnight August 1, 2010')
# Specify the y-axis label
plt.ylabel('Temperature (degrees F)')
# Display the plot
plt.show()

# To plot dataframes with multiple columns we can use the same pandas plot method
# There are many optional parameters or ways to cutomize plot for dataframes with multiple columns
df2 = pd.DataFrame({'Temperature (deg F)': [79.0, 78.9, 76.5, 77.7], 
                    'Pressure (atm)': [1.0, 1.0, 1.0, 1.0],
                    'dew point (deg F)': [68.9, 67.5, 69.0, 66.8]})
# Default is, this will plot all columns on a single plot
df2.plot()
# we can plot all columns on different subplots in a single plot
df2.plot(subplots=True)

# or we can plot some columns out of the dataframe at once
df2[['Temperature (deg F)', 'dew point (deg F)']].plot()



"""
2.1. Visual exploratory data analysis
"""

df3 = pd.DataFrame({'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
                    'Temperature (deg F)': [79.0, 78.9, 76.5, 77.7], 
                    'Pressure (atm)': [1.0, 1.0, 1.0, 1.0],
                    'dew point (deg F)': [68.9, 67.5, 69.0, 76.8],
                    'country': ['India', 'USA', 'Japan', 'China']})
df3.set_index('Month', inplace=True)
print(df3)

# Suppose we want Month column on x-axis and Temperature and Pressure column on y-axis then we can do like below
df3[['Temperature (deg F)', 'Pressure (atm)']].plot()

# we can also specify different kinds of plot by using kind argument
df3.plot(x = 'dew point (deg F)', y = 'Temperature (deg F)', kind = 'scatter')

# Generate box plots of multiple columns from dataframe
df3[['Temperature (deg F)', 'dew point (deg F)']].plot(subplots = True, kind='box')

# PROBABILITY DENSITY AND CUMULATIVE DENSITY FUNCTIONS
# histograms are great for plotting Probability density functions and Cumulative density functions
# To find PDF (Probability density function) plot, specify argument normed=True
df3['Temperature (deg F)'].plot(kind='hist', bins=10, normed=True)

# To find CDF (Cumulative density function) plot, specify argument normed=True and cumulative=True
df3['Temperature (deg F)'].plot(kind='hist', bins=10, normed=True, cumulative=True)

df3.plot.bar()
df3.plot.hist(alpha=0.5, orientation='horizontal')



"""
2.2. Statistical exploratory data analysis
"""

# Finding min, max, mean, median, standard deviation
print(df3['Temperature (deg F)'].min())
print(df3['Temperature (deg F)'].max())
# Construct the mean percentage per Month
mean = df3.mean(axis='columns')
print(mean)
mean.index = ['Jan', 'Feb', 'Mar', 'Apr']
mean.plot()

# we can also find any quantile
df3.quantile([0.05, 0.95])
# To find standard deviation of columns use std() function on the dataframe
print(df3.std())


"""
3.1. Indexing time series in pandas
"""

# if a csv file contains datetime in some columns, we can specify additional argument parse_dates = True to read_csv function
# it will read strings into datetime objects in ISO 8601 format (yyyy-mm-dd hh:mm:ss)
# specifying index_col = 'Date' will make Date column as index so that we can slice data using dates
df_datetime = pd.read_csv('filename.csv', parse_dates=True, index_col = 'Date')
# this line will select company value on datetime 2015-02-02 11:00:00
df_datetime.loc['2015-02-02 11:00:00', 'Company']
# we can select whole day also or whole month
df_datetime.loc['2015-02-02']
# we can also use
df_datetime['February 5, 2015']
# for month we do
df_datetime.loc['2015-02']

# we can also slice using range of dates
df_datetime.loc['2015-02-16':'2015-02-20']

# To convert datetime as strings into datetime objects we use pandas to_datetime method
datetime_list = pd.to_datetime(['2015-02-02 11:00:00', '2015-02-16 08:08:08', '2015-02-15 06:00:34', '2015-02-08 01:15:23'])
print(datetime_list)
# reindex method is used to match a new index with existing date time index of a pandas series or dataframe


"""
3.2. Resampling pandas time series
"""

# Applying statistical methods (mean, std etc) over different time intervals
# suppose a dataframe is there in which index is datetime and other columns are present with some columns having numerical data
# now we need to get mean of numerical columns for each day
# non numeric columns will be ignored in this case
daily_mean = sales.resample('D').mean()
daily_sum = sales.resample('D').sum()
# 'D' is used for day, 'W' is used for week, `

weekly_count = sales.resample('W').count()
# Downsampling: reduce datetime rows to slower frequency
# Upsampling: increase datetime rows to faster frequency


"""
3.3. Manipulating pandas time series
"""

# Using .str.method() to manipulate pandas dataframe columns
# for working example see Bakery data kernel on kaggle
print(bakery['Item'].str.upper())
print(bakery['Item'].str.contains('Coffee').sum())

# Using .dt.method() to manipulate pandas columns with datetime objects
print(bakery['date_time'].dt.hour.head())
print(bakery['date_time'].dt.tz_localize('US/Central').dt.tz_convert('US/Eastern').head())

print(list('ABCD'))

"""
3.4. Visualizing pandas time series
"""

# Line types, plot types and subplots
# For dataframes with datetime as index the plot function will automatically use datetime on x-axis


