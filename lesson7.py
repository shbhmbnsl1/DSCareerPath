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
    2.1. Tidy Data (Melting data)
    2.2. Pivoting data
    2.3. Beyond melting and pivoting
    
3. Combining data for analysis
    3.1. Concatenating data
    3.2. Concatenating many files (Finding and concatenating)
    3.3. Merge data
    
4. Cleaning data for analysis
    4.1. Data types
    4.2. Using regular expressions to clean data
    4.3. Using functions to clean
    4.4. Duplicate and missing data
    4.5. Testing with asserts
    
5. Conclusions

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
# read more about describe method on https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.describe.html
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
# to read more about pandas plot function read https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.plot.html
df['Existing Zoning Sqft'].plot(kind='hist', rot=70, logx=True, logy=True)
# Display the histogram
plt.show()


# VISUALIZING MULTIPLE VARIABLES USING BOXPLOTS
# Histograms are great ways of visualizing single variables.
# To visualize multiple variables, boxplots are useful, especially when one of the variables is categorical
# The pandas .boxplot() method is a quick way to compare two columns,
# in which you have to specify the column and by parameter
# Import necessary modules
import pandas as pd
import matplotlib.pyplot as plt
# Create the boxplot
# we can also provide list of column names in both column and by params
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


"""
2.2. Pivoting data

"""
# PIVOTING opposite of melting
# We turn unique values into columns
# This line will pivot column measurement
# While melting takes a set of columns and turns it into a single column, 
# pivoting will create a new column for each unique value in a specified column
# index parameter is used for columns which we dont want to be pivoted
# columns param is the columns to be pivoted
# values param is the values to be used to pivot the columns
airquality_pivot = airquality_melt.pivot_table(index=['Month', 'Day'], columns='measurement', values='reading')

# after running above line of code we didnt get the actual dataframe. Instead we got a dataframe with multiindex
# reset_index is the method used to get back the original df from pivoted df
airquality_pivot_reset = airquality_pivot.reset_index()

# if duplicate rows exist then pivot_table method will show error
# to fix duplicate rows we can use aggfunc parameter 
# here aggfunc=np.mean means that mean of duplicate values will be taken
airquality_pivot = airquality_dup.pivot_table(index=['Month', 'Day'], columns='measurement', values='reading', aggfunc=np.mean)


"""
2.3. Beyond melting and pivoting
"""

# Some coliumns might contain mixed values like variable column in below dataframe
# it containes value like m014 which denotes sex m and age range 0-14
# to clean this column we create two new colums by extracting the characters of values from variable column
# one column is for sex
# second column is for age-group
import pandas as pd
random_df = pd.DataFrame({'country':['AD','AE','AF','AD','AE','AF'], 
                          'year':[2000,2000,2000,2000,2000,2000], 
                          'variable':['m014','m014','m014','m1524','m1524','m1524'], 
                          'value':[0, 2, 24, 0, 4, 228]})
print(random_df)
random_df['sex'] = random_df.variable.str[0]
random_df['age_group'] = random_df.variable.str[1:]
print(random_df)


"""
3.1. Concatenating data
"""

# concatenating dataframes can be done by using pandas concat function
# suppose we have two dataframes
df1 = pd.DataFrame({'name':['Shubham', 'John', 'Raj'], 'age':[21, 34, 36], 'sex':['M','M','M']})
df2 = pd.DataFrame({'name':['Rahul', 'Sanju', 'Sita'], 'age':[23, 33, 38], 'sex':['M','M','F']})
concate = pd.concat([df1,df2], ignore_index = True)
print(concate)

# Concatenating data column wise
# column-wise concatenation of data as stitching data together from the sides instead of the top and bottom
# we will concatenate df1 and df3 which should be column wise
# to concatenate column wise provide additional argument axis=1
df3 = pd.DataFrame({'occupation': ['Student','Employee','Businessman'], 'location': ['JP','MUM','BLR']})
column_concat = pd.concat([df1, df3], axis=1)
print(column_concat)


"""
3.2. Finding and concatenating data (from files)
"""

# If there is a large number of files which need to be read then we can use glob function to find file names based on pattern
# Globbing: Pattern matching for file names
# glob method will take one argument which is the pattern to match for file names
# In the below case it will return a list of all file names with .csv extension
# Next it will read each file's content as a dataframe by entering a for loop and then append each dataframe to a common list
# this list of data frames will then be concatenated using pandas concat function
import glob
files_list = glob.glob('*.csv')
data_frames = []
for file_name in files_list:
    df = pd.read_csv(file_name)
    data_frames.append(df)
concatenated_dataFrame = pd.concat(data_frames)


"""
3.3. Merge data
"""

# Merging is similar to joins in SQL
# Merging is combining disparate datasets based on common columns
state_populations = pd.DataFrame({'name':['Rajasthan', 'Gujarat', 'Maharastra', 'Punjab'], 'population':[20000, 10000, 40000, 50000],
                                  'geography': ['Desert', 'Plain', 'Valley', 'Agriculture']})
state_codes = pd.DataFrame({'state':['Gujarat', 'Punjab', 'Rajasthan', 'Maharastra'], 'code':['GUJ','PUN','RAJ','MAH'],
                            'geo': ['Plain', 'Agriculture', 'Desert', 'Valley']})
merged_df = pd.merge(left = state_populations, right = state_codes, on = None, left_on = ['name', 'geography'], right_on = ['state', 'geo'])
print(merged_df)


"""
4.1. Data types
"""

# to get data types for each column of a dataframe
print(df.dtypes)
# to convert a column to a string type we pass str to the astype method of the dataframe's column
df['population'] = df['population'].astype(str)

# Some variables may represent category such as sex 
# for such columns we can pass category to astype method
df['sex'] = df['sex'].astype('category')

# if numeric data is stored as string type then we can convert it using pandas to_numeric method
# passing errors as coerce will convert invalid values such as - to NaN
# if we do not pass errors=coerce python will return error
df['population'] = pd.to_numeric(df['population'], errors = 'coerce')

"""
4.2. Using regular expressions to clean data

Examples of regular expressions for matching different types of patterns

17         \d*
$17        \$\d*
$17.00     ^\$\d*\.\d{2}$
"""

# regular expressions are used to do pattern matching
# Compile the pattern
# use the compiled pattern to match values
import re
# Compile the pattern: prog
prog = re.compile('\d{3}-\d{3}-\d{4}')
# See if the pattern matches
result = prog.match('123-456-7890')
print(bool(result))
# See if the pattern matches
result2 = prog.match('1123-456-7890')
print(bool(result2))

# FINDALL function
# to find all occurrences of a pattern in a string we use findall function
# Find the numeric values: matches
matches = re.findall('\d+', 'the recipe calls for 10 strawberries and 1 banana')
print(matches)

# directly match without compiling
pattern1 = bool(re.match(pattern='\d+', string='123-456-7890'))
print(pattern1)


"""
4.3. Using functions to clean
"""
# Refer datacamp 
def cleaning_function(row): 
    return something

df.apply(cleaning_function, axis=1)

"""
4.4. Duplicate and missing data
"""

# to drop duplicate rows of data from data frame we use drop_duplicates method on the data frame
df = df.drop_duplicates()

# MISSING DATA
# Three ways to deal with missing data
# 1. Leave as-is
# 2. Drop them
# 3. Fill missing value
# use info() method to know how much missing data

# Drop missing data
df_dropped = df.dropna()

# Fill missing values using fillna() method
# below line will fill missing values in sex column with 'missing'
random_df['sex'] = random_df['sex'].fillna('missing')

# we can fill missing values in a column with some statistics value
mean_salary = random_df['salary'].mean()
random_df['salary'].fillna(mean_salary)


"""
4.5. Testing with asserts
"""

assert 1 == 1
assert 1 == 2


"""
5. Conclusions: 
    Steps of data cleaning:
        1. Explore and visualize data:
            using methods and attributes such as info, columns, head, shape, plot etc.
        2. Concatenate and merge data if present in many different dataframes:
            using concat and merge methods
        3. Reshape data:
            using melting and pivoting ideal for your use case, also 
        4. Check data types and change data types of data:
            using dtypes, to_numeric, astype methods and test using assert statements when done
        5. Look at spelling errors: 
            using patterns, regular expressions, findall(), match functions
        6. Clean duplicates: 
            using drop_duplicates
        7. Clean missing data:
            using dropna(), fillna() functions and test using assert functions
"""

