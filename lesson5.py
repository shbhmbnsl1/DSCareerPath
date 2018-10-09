#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 23:03:03 2018

@author: shubansa
Data Science Career Path - Lesson 5
"""

"""
1. Importing text file
"""
file = open('titanic.txt', mode='r')
content = file.read()
file.close()

# if we don't want to worry about closing the file each time we can use with
# this is the best practice
with open('simple_exp.py', mode='r') as file :
    content2 = file.read()
    print(content2)

# we can also read only some lines of the files
with open('simple_exp.py', mode='r') as file:
    print(file.readline())
    print(file.readline())





"""
2. Importing flat files using numpy
"""

# To import flat files containing data of only a single type we can use numpy 
# file data is imported as numpy array by specifying the delimiter 
# if the file contains some header we can skip that row using additional argument skiprows
# we can also select only some columns by using the argument usecols 
# 
import numpy as np
data = np.loadtxt('file.txt', delimiter=',')

file = 'digits_header.txt'
data = np.loadtxt(file, delimiter='\t', skiprows=1, usecols=[0,2])

# we can also import file as a single data type by specifying dtype as an additional argument
data_float = np.loadtxt(file, delimiter='\t', dtype=float, skiprows=1)

# to work with mixed datatypes genfromtxt is used
# this numpy method takes three arguments 
# @param filename, delimiter, names: True means a header is present, 
# dtype is specified as None to work with mixed datatypes
# @returns a 1D array which has each element as one row of the flat file as a tuple
data = np.genfromtxt('titanic.csv', delimiter=',', names=True, dtype=None)

# recfromcsv and genfromtxt are same but in recfromcsv delimiter and names and dtype have default values
d = np.recfromcsv(file)


"""
3. Importing flat files using pandas
"""

import pandas as pd
data = pd.read_csv('titanic.csv')
print(data.head())

# to select only some rows from the csv file
data2 = pd.read_csv('titanic.csv', nrows=5, header=None)
data_array = data2.values
print(data_array)

# if some file has comments and missing values
data3 = pd.read_csv('titanic.txt', sep='\t', comment='#', na_values='Nothing')
print(data3.head())


"""
4. Importing other types of files like excel, matlab, sas, stata and hdf5 And pickled files
"""                  

# Pickled files are serialized files used to store data structures as bytestream
import pickle
with open('data.pkl', 'rb') as file:
    d = pickle.load(file)
print(d)

# Importing excel files
import pandas as pd
xl = pd.ExcelFile('fileName.xlsx')
print(xl.sheet_names) # As excel file contains a lot of sheets this line will print all the sheet_names in excel file
# To load a particular sheet from excel file. This returns a DataFrame
df1 = xl.parse('any_sheet_name')
# We can also pass index of sheet name in parse function
df2 = xl.parse(0)

# Customizing spreadsheet imports
# this will skip first row and rename the columns with names specified
df1 = xl.parse(0, skiprows=[0], names=['Country','AAM due to War (2002)'])

# this will parse only first column of the sheet, skip first row and rename the column to Country
df2 = xl.parse(1, parse_cols=[0], skiprows=[0], names=['Country'])


"""
4.1 Importing SAS data and Stata
SAS - Statistical Analysis System
Stata - statistics and data
"""

# importing SAS files
import pandas as pd
from sas7bdat import SAS7BDAT
with SAS7BDAT('sales.sas7bdat') as file:
    df_sas = file.to_data_frame()
    
# importing stata file
df = pd.read_stata('disarea.dta')


"""
4.2 Importing HDF5 files
HDF5 - Heirarchical data format version 5
"""
# HDF5 files are used to store large quantities of numerical data
# datasets can be hundreds or gigabytes or terabytes
import h5py
file = 'LIGO_data.hdf5'

# Load file: data
data = h5py.File(file, 'r')

# Print the datatype of the loaded file
print(type(data))

# Print the keys of the file
for key in data.keys():
    print(key)

# Extract some key from data
group = data['some_key']
for keys in group.keys():
    print(keys)
    
"""
4.3 Importing Matlab files
"""

# for matlab files scipy library is used
import scipy.io
mat = scipy.io.loadmat('filename.mat')
# printing type of mat returns dictionary
# in this dict keys-names of matlab variables and values-object assigned to variables
print(type(mat))
print(mat.keys())
print(tyep(mat['x']))




"""
5. Introduction to relational databases
"""

# Creating database engine in Python
# SQLAlchemy package is used to import relatonal databases
# Import create_engine function from sqlalchemy module
from sqlalchemy import create_engine
# Create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')
# Save the table names to a list: table_names
table_names = engine.table_names()
# Print the table names to the shell
print(table_names)

"""
Querying the relational database
-- Complete Workflow --
1. Import packages and functions
2. Create the engine
3. Connect to the engine
4. Query the database
5. Store the result of query
6. Close the connection
"""

from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('sqlite:///Chinook.sqlite')

con = engine.connect()

rs = con.execute("SELECT * FROM Orders")

df = pd.DataFrame(rs.fetchall())
df.columns = rs.keys()


# We can also fetch only a specific number of rows by using fetchmany function instead of fetchall
df2 = pd.DataFrame(rs.fetchmany(size=5))

con.close()

print(df.head())


"""
Same workflow with context manager
"""
from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('sqlite:///Chinook.sqlite')

with engine.connect() as con:
    rs = con.execute("SELECT * FROM Orders")

    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()


    # We can also fetch only a specific number of rows by using fetchmany function instead of fetchall
    df2 = pd.DataFrame(rs.fetchmany(size=5))
    
"""
Using pandas to run query and get data instead of whole workflow
"""
df = pd.read_sql_query("SELECT * FROM Employee", engine)

# We can run any query from this functions



