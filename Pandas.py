#!/usr/bin/env python
# coding: utf-8

# # Pandas

# One of the most popular data wrangling packages.It built on the another package Numpy.

# . Data cleansing
# 
# . Data fill
# 
# . Data Normalization
# 
# . Merges and Joins
# 
# . Data visualization
# 
# . Statistical Visualization
# 
# . Data Inspection
# 
# . Loading and Saving Data

# Pandas generally provide two data structures for manipulating data 
# 
# 1.Series 
# 
# 2.DataFrame

# .Series is the one dimensional array which cabaple of holding data of any data type. The axis labels are colectively called <b> indexes </b> 

# .DataFrame is two dimensional , mutable, potentinally heterogeneous tabular data structure with labeled axes.It consists of three principle components data,rows, and columns 

# In[1]:


import pandas as pd
import numpy as np


# In[5]:


import warnings
warnings.filterwarnings('ignore')
# creating empty series
ser1 = pd.Series ()
print(ser1)

# simple array
data = np.array(['p','a', 'n' , 'd', 'a','s'])
print(data)

ser2 = pd.Series(data)
print(ser2)


# In[8]:


df = pd.DataFrame()
print(df)

# list of string
list = ['data' , 'wrangling' , 'packages']
print(list)

# calling dataframe constructor on list
df = pd.DataFrame(list)
print(df)


# In[11]:


data = {
    "col1" : [10,20,30,40],
    "col2" : [50,60,70,80]
}

df = pd.DataFrame(data)
print(df)

print(type(df))


# # Pandas Series

# One dimentional object array or list or column 

# In[23]:


# Sample series
seires1 = pd.Series([1,2,3,"string" ,4.3 , -34])
print(seires1)
print(seires1[0])


# In[14]:


# adding custom index
index = ['a' , 'b' , 'c' , 'd' , 'e' , 'f']
seires2 = pd.Series([1,2,3,"string" ,4.3 , -34] , index=index)
seires2


# In[18]:


# acessing the elements in list
print(seires2['a'])
print(seires2['d'])


# creating series using dictionaries

# In[20]:


series3 = pd.Series({'london':20,'uk':30,'germany':40})
series3


# In[21]:


series3['germany']


# In[22]:


# logocal operations
series3[series3 >25]


# In[24]:


s1 = pd.Series([1,2,3])
s2 = pd.Series([4,5,6])
s3 = s1>s2
print(s3)


# In[29]:


s4 = pd.Series((4,5,6) )
               
print(type(s4))


# # DataFrames

# In[31]:


# Sample data frame
column1 = ['A', 'B','C','D','E']
column2 = [10,20,30,40,50]

df= pd.DataFrame( { 'names':column1 , 'marks':column2 })
df


# In[32]:


# get first 3 rows
df.head(3)


# In[33]:


# get last 2 rows
df.tail(2)


# In[34]:


# columns
df.columns


# In[35]:


# change the column names
df.columns = ['stu_names' , 'stu_marks']
df


# In[36]:


# change the row names
df.index = ['a1' , 'b1' , 'c1' ,'d1' , 'e1']
df


# In[37]:


# accessing only one column
df['stu_marks']


# In[40]:


# delete single column
del df['stu_names']
df


# In[43]:


column1 = ['aby' , 'nan' , 'ash' , 'stu' , 'meg']
column2 = [80,27,89,90,68]
column3 = ['B' , 'D' , 'A' , 'A' , 'C']

df = pd.DataFrame({'names':column1 ,'marks':column2 , 'grade':column3})
df


# In[44]:


# access rows index 1 to 4
df.iloc[1:4]


# In[45]:


# access rows index 1 to 4 only the grade column
# df row column
df.iloc[1:4 , 2]


# In[46]:


# all rows and columns
df.iloc[: , :]


# In[48]:


# students who got marks >30
df[df['marks'] > 30]


# In[49]:


# students who got grade A
df[df['grade'] == 'A']


# In[51]:


# access multiple columns
df[['names','marks']]


# In[52]:


df.names


# <b> Concatenation </b>

# Concatenate two dataframes either vertically or horizontally

# In[56]:


# first datafreame
column1 = ['aby' , 'nan' , 'ash' , 'stu' , 'meg']
df1 = pd.DataFrame({'names' :column1}) 
df1


# In[57]:


column2 = [50,60,90,87,75]
df2 = pd.DataFrame({'marks' :column2}) 
df2


# axis = 1 is for Horizontally axis = 0 is for vertically 

# In[59]:


df3 = pd.concat([df1,df2] , axis=1 , ignore_index =True)
df3


# # apply() method

# syntax:
# 
# dataframe.apply(func , axis , raw , result_type , args , kwds)

# In[60]:


# dictionary with three fields each
data = {
    
    'prodcut_Id':[1,2,3,4,5],
    'Category':['A', 'B' , 'C' , 'A' ,'C'],
    'availableStock':[2,5,8,3,5],
    'priceperunit':[300000,25000,56000,61000,470000]
}
# converting in to fata frame
df = pd.DataFrame(data)
print(df)


# In[61]:


df['priceperunit_in_thousands'] = df['priceperunit'].apply(lambda x : x/1000)
df.head()


# In[62]:


df['total_revenue'] = df.apply( lambda row: row['availableStock'] * row['priceperunit'] , axis = 1)
df


# In[63]:


df['total_revenuein_thousands'] = df['total_revenue'].apply(lambda x : x/1000)
df.head()


# # Indexing DataFrames

# In[64]:


columna = ['aby' , 'nan' , 'ash' , 'stu' , 'meg']
columnb = [80,27,89,90,68]
columnc = ['B' , 'D' , 'A' , 'A' , 'C']

df = pd.DataFrame({'names':columna ,'marks':columnb , 'grade':columnc})
df


# In[65]:


# acess row index 1 to 3
df.iloc[1:4]


# In[67]:


# accessing single column names
df['names']


# In[70]:


# multiple columns
df[['names' , 'marks']]


# In[74]:


# marks and grade scored by the student aby
df[df['names'] == 'aby']  [['marks' , 'grade']]


# In[75]:


df.index=['a','b','c','d','e']
df


# In[76]:


df.loc['c']


# In[80]:


df.loc['e'] [['marks' , 'grade']]


# In[81]:


df.iloc[4] [['marks' , 'grade']]


# # GroupBy

# .pandas dataframe.groupby() functionis used to split the data into groups based on some criteria.
# 
# .using for grouping the data according to the categories and apply a function to the categories(min,max, avg,sum)

# In[90]:


columnx = ['aby' , 'nan' , 'ash' ,'aby' , 'nan' , 'ash','aby' , 'nan' , 'ash' ]
columny = [80,27,89,90,68,70,65,40,97]
columnz = ['mat','phy','social','mat','phy','social','mat','phy','social']

df = pd.DataFrame({'names':columnx ,'marks':columny , 'subject':columnz})
df


# In[92]:


# top marks
df.groupby('names').agg('sum')


# In[93]:


df.groupby('names').agg('mean')


# # Date Range

# .Use ful for creating range of times and dates
# 
# .mainly used to reindexing our Datetime index 

# format:
# 
# pd.date_range(start_time , end_time)

# In[96]:


pd.date_range(start= '2022-10-10' , end='2022-11-10' , freq='D')


# In[97]:


# split the date time in 6 minites interval
pd.date_range(start= '2022-10-10 00:00:00' , end='2022-10-10 00:24:00' , freq='6T')


# In[98]:


# creating date range with 10 equal periods 
pd.date_range(start= '2022-10-10 00:00:00' , end='2022-10-10 00:24:00' , periods=10)


# In[101]:


# all working days between two time intervals
# ferq = 'B' = business days
pd.date_range(start= '2022-01-01 00:00:00' , end='2022-01-10 00:24:00' , freq = 'B')


# In[103]:


# week day----------freq = 'W'
pd.date_range(start= '2022-01-01 00:00:00' , end='2022-03-10 00:24:00' , freq = 'W')


# In[104]:


# months -------freq = 'M'
pd.date_range(start= '2022-01-01 00:00:00' , end='2022-05-10 00:24:00' , freq = 'M')


# In[105]:


# quaters ---freq = 'Q'

pd.date_range(start= '2022-01-01 00:00:00' , end='2022-05-10 00:24:00' , freq = 'Q')


# In[106]:


df = pd.DataFrame({'A':[1,2,3] , 'B' :[4,5,6]})
print(df.mean())


# In[110]:


df = pd.DataFrame({'A':[1,2,3] , 'B' :[4,5,6]})
df['C'] = df.apply(lambda x:x['A'] + x['B'] , axis =1)
print(df)


# In[112]:


data = pd.DataFrame({'name':['a','b','c'] , 'age' :[24,15,56]})
df = pd.DataFrame(data)

print(df.loc[df['age']>30])


# In[117]:


df = pd.DataFrame({'A':[1,2,3] , 'B' :[4,5,6]})
print(df.mean())


# In[ ]:





# In[ ]:




