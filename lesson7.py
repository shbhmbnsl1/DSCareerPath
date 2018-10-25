# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 16:03:53 2018

@author: shbhm
Data Science Career Path - Lesson 7 Cleaning Data in Python
"""

"""
1. Exploring your data
    1.1. Diagonizing data
    1.2. Exploratory data analysis
    1.3. Visual exploratory data analysis

2. Tidying data for analysis
    2.1. Tidy Data
"""


"""
1.1. Diagonizing data
"""

# Import pandas
import pandas as pd
# Read the file into a DataFrame: df
df = pd.read_csv('dob_job_application_filings_subset.csv')
# Print the head of df
print(df.head())
# Print the tail of df
print(df.tail())
# Print the shape of df
print(df.shape)
# Print the columns of df. This will print the name of all columns in the dataframe
print(df.columns)
# Print the info of df
print(df.info())


"""
1.2. Exploratory data analysis
"""

# Using descibe method we can get the count, std, min, 25%, 50%, 75% and max for all numeric columns
print(df.describe())

# For exploring categorical data we can use value_counts method on any column from the dataframe
# value_counts method will give us the frequency counts for each unique value in a column
# This method also has an optional parameter called dropna which is True by default. 
# What this means is if you have missing data in a column, it will not give a frequency count of them. 
# We set the dropna column to False so if there are missing values in a column, we get the frequency counts
# Print the value counts for column 'Borough'
print(df['Borough'].value_counts(dropna=False))

"""
1.3. Visual exploratory data analysis
"""
# Import matplotlib.pyplot
import matplotlib.pyplot as plt
# Plot the histogram
# select column for which we want to plot the histogram
# use the plot function
# provide necessary args
df['Existing Zoning Sqft'].plot(kind='hist', rot=70, logx=True, logy=True)
# Display the histogram
plt.show()


# VISUALIZING MULTIPLE VARIABLES USING BOXPLOTS
# Histograms are great ways of visualizing single variables. 
# To visualize multiple variables, boxplots are useful, especially when one of the variables is categorical
# The pandas .boxplot() method is a quick way to compare two columns, 
# in which you have to specify the column and by parameters
# Import necessary modules
import pandas as pd
import matplotlib.pyplot as plt
# Create the boxplot
df.boxplot(column='initial_cost', by='Borough', rot=90)
# Display the plot
plt.show()

# VISUALIZING MULTIPLE VARIABLES USING SCATTER PPOTS
# Boxplots are great when you have a numeric column that you want to compare across different categories.
# When you want to visualize two numeric columns, scatter plots are ideal
df.plot(kind='scatter', x='initial_cost', y='total_est_fee', rot=70)
plt.show()


"""
2.1. Tidy data

Note: Tidy data paper Hadley Wickham

Principles of tidy data: 
    a. Columns represent separate variables
    b. Rows represent individual observations
    c. Observational units form tables
"""

# MELTING columns of data frame
# In melting we turn columns into rows
# this line will melt all columns(other than column Month & Day) of data frame airquality into a single column
# Melting the columns may make the data untidy but it will be better in some scenarios
airquality_melt = pd.melt(frame=airquality, id_vars=['Month', 'Day'])
# add custom names to variable column and value column after melting colums
airquality_melt = pd.melt(frame=airquality, id_vars=['Month', 'Day'], var_name='measurement', value_name='reading')

# PIVOTING opposite of melting
# We turn unique values into columns
# This line will pivot column measurement 
airquality_pivot = airquality_melt.pivot_table(index=['Month', 'Day'], columns='measurement', values='reading')


