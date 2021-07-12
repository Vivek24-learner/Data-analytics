# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 03:20:28 2021

@author: HP
"""

import pandas

# Reading CSV Files with Pandas:
df = pandas.read_csv('C:/Users/HP/Desktop/Data')
print(df)

# Writing CSV Files with Pandas:
df.to_csv('C:/Users/HP/Desktop/Data1')

# Reading Excel Files with Pandas
df1 = pandas.read_excel('C:/Users/HP/Desktop/Data/Excel')

df1 = pandas.read_excel('User_Data.xlsx')
print(df1)

# Writing Excel Files with Pandas 
df1.to_excel('IIT-B.xlsx')
df2 = pandas.DataFrame(df1)
print (df2)