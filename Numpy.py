#!/usr/bin/env python
# coding: utf-8

# # Numpy

# Numpy means Numerical python.Is a Python Library for Numerical Calculations.
# 
# .Numpy built on Linear algebra.Its about matrices and vectorsand performing mathematical calculatuons on them.
# 
# . Key concept in numpy is array data type.
# 
#         One dimensional arrays:vectors
#         
#         Two dimensional arrays:Matrices
#                 
#         Three dimensional arrays:Tensors
#             
#             
# . Numpay arrays requires <b> homogeneous </b> data types.that is it will allows only one data type of all elements.
# 
# . Important library for Data science, machine learning, signal and image processing, Scientific and engieer computing.

# In[1]:


# import
import numpy as np


# In[2]:


# new numpy array
nparray = np.array([1,2,3,4,5,6,7,8,9,10])
print(nparray)
print(type(nparray))


# <b> Numpy Array Dimensions </b>
# 
# 1. One dimensional
# 
# 2. Two dimensional
# 
# 3. THree dimensional

# In[3]:


import numpy as np


# <b> Scalar Array </b>

# Array which contain only one element

# In[4]:


Scalar = np.array(5)
Scalar


# In[5]:


print(np.ndim(Scalar))


# <b> One dimensional </b>

# In[6]:


A=np.array([1,2,3,4,5])
print(A)
print(type(A))
print(np.ndim(A))


# <b> Two dimensional </b>

# In[7]:


b = [[1,2,3],[5,6,7],[8,9,10]]
B=np.array(b)
print(B)
print(type(B))
print(np.ndim(B))


# <b> Three dimensional </b>

# In[8]:


c = [[ [1,2] , [3,4]] , [[5,6] , [7,8] ] , [[9,10] , [11,12]] ]
C=np.array(c)
print(C)


# In[9]:


print(type(C))
print(np.ndim(C))


# In[10]:


print(A.ndim)
print(B.ndim)
print(C.ndim)


# # List vs Numpy Array 

# <b> Similarities </b>

# 1.used to store data
# 
# 2.both are mutable
# 
# 3.both can be indexed
# 
# 4.Can perform slicing operation

# <b> Differences </b>

# <b> 1. List contains different data types but numpy array can contain similar data types. </b>

# In[11]:


list = [1,2,3,'a','pen']
print(list)


# In[12]:


Narray = np.array([1,2,3,4,5])
print(Narray)


# In[13]:


Narraylist = np.array([1,2,3,'a','pen'])
print(Narraylist)


# Converted all in to string

# <b> 2.Way of Performing Operations </b> 

# In[14]:


arr = np.array([1,2,3,4,5])
print(arr)
print(type(arr))


# In[15]:


arr/5


# In[16]:


list1 = [1,2,3,4,5]
print(list1)
print(type(list1))


# In[17]:


# list1/5
# type error


# <b> Advantages of Numpyarrays over List </b>

# 1.Numpy arrays consumes less memory
# 
# 
# 2.Faster than List

# In[18]:


#Create a numpy array using arange with 1 and 11 as parameter in it
arrange = np.arange(1,11)
arrange


# In[19]:


# Create an array using arange passing 1,11 and 2 as parameter in iter
arrange1 = np.arange(1,11,2)
arrange1


# In[20]:


# create numpy array using eye function with 3 as passed parameter
Eye = np.eye(3, k=1)
Eye


# In[21]:


#create a numpy array using zero function with (3,2) as passed parameter

zeors = np.zeros((3, 2))
zeors


# In[22]:


#create a numpy array using ones function with (3,2) as passed parameter

ones = np.ones((3, 2))
ones


# In[23]:


#create a numpy array using full function with (3,3) and 2 as passed parameter
full = np.full((3, 3), [2])

full


# In[24]:


#create a numpy array using diag function passing a list [1,2,3,4,5]
diag = np.diag([1,2,3,4,5])
diag


# In[25]:


# Create a numpy array v with [1,2,3] as its elements
v = np.array([1,2,3])



#Use tile function of numpy and pass v and (3,1) as its parametrs
tile = np.tile(v,(3,1))
tile


# In[26]:


# Create an array with 100 values between 1 and 50 using linspace
linspace = np.linspace(1, 50, num=100)
linspace


# # Numpy Array Reshaping

# In[31]:


R = np.arange(12)
print(R)
print(type(R))
print(R.ndim)


# <b> Reshaping into Two Dimentional Array </b>

# In[33]:


new_R = R.reshape(2,6)
print(new_R)
print(new_R.ndim)


# In[35]:


new_R1 = R.reshape(3,4)
print(new_R1)
print(new_R1.ndim)


# <b> 2D to 1D Array </b>

# In[38]:


new_R2 =np.array( [[1,2,3],[5,6,7],[8,9,10]] )
print(new_R1)
print(type(new_R2))
print(new_R2.ndim)


# In[39]:


# 9 means , 9 elements
new_R3 = new_R2.reshape(9)
print(new_R3)
print(new_R3.ndim)


# . If don't know the exact dimensions for conversions we can use -1 , so that numpy will figure it out the correct dimensions

# In[40]:


R4 =np.array( [[1,2,3,4],[5,6,7,8],[9,10,11,12]] )
print(R4)
print(R4.ndim)


# In[41]:


new_R4 = R4.reshape(4,-1)
print(new_R4)


# <b> : -1 can be used to flatten an array which means converting a multidimensional array into a 1D array. </b>

# In[42]:


F=np.arange(1,17)
print(F)


# In[43]:


F1 = F.reshape(2,4,2)
F1


# In[44]:


F2 = F1.reshape(-1)
F2


# # Numpy Array Indexing

# . zero based Indexing
# 
# . Negative indexing also posssible

# In[45]:


N=np.array([1,2,3,4])
print(N)
print(type(N))


# In[48]:


# Accessing 4 th element
# positive Indexing
print(N[3])
# negative Indexing
print(N[-1])


# In[49]:


# Accessing 2 nd element
# positive Indexing
print(N[1])
# negative Indexing
print(N[-3])


# <b> Acessing Two Dimentional Array </b>
# 
# in matrices <b> i  </b> represents <b> rows </b> and <b> j </b> represents <b> columns </b>

# In[53]:


# Two dimensional Array
TD = np.array ([[1,2] , [3,4]] )
print(TD)
print(TD.shape)


# In[56]:


# Acessing 1st element  --- which is in O th row and 0 th column 
print(TD[0][0])

# for other elements
print(TD[0][1])
print(TD[1][0])
print(TD[1][1])


# In[61]:


# Negative Indexing
print(TD[-2][-2])
print(TD[-2][-1])
print(TD[-1][-2])
print(TD[-1][-1])


# <b> Acessing Three Dimentional Array </b>

#  i-----matrix index
#     
#  j-----rows
#     
#   k-----columns   

# In[63]:


TD = np.arange(1,19)
print(TD)


# In[65]:


TD1 = TD.reshape(2,3,3)
print(TD1)


# In[68]:


# acessing element 3 , it is in 0th matrix , 0 st row and 2 rd col
print(TD1[0][0][2])

# Negative Indexing
print(TD1[-2][-3][-1])


# In[71]:


TD2 =np.array( [[1,2,3],[4,5,6],[7,8,9]] )
print(TD2[1])
x123 = TD2[-2 , -1]
x123


# # Slicing Operation

# to retrieve collection of values
# 
# start= inclusive , starting index
# 
# end = exclusive , ending index
# 
# step =difference between index ( optional default 1) 
# 
# 

# In[73]:


S = np.array([1,4,7,11,6,3])
print(S)


# In[78]:


# get the elements 4,7,11
print(S[1: 4: 1 ])

# 4=Starting position is 1
# for 7 = ending positon is 4
# step= 1 (optional)


# In[79]:


# get 1,4,7
print(S[0: 3: 1])


# . if we skip the start index it will start form 0 index.
# 
# . if we skip the end index it will go till last.
# 
# . for step the default will be 1.

# In[81]:


# first three elements 
print(S[0: 4])
print(S[: 4])


# In[82]:


# get all elements from 2 index to last
print(S[2:])


# In[86]:


# elements with step size 2
print(S)
print(S[::2])


# In[87]:


# to get all elements
print(S[::])


# # Two Dimensional Array

# In[89]:


S1 = np.array([[4,7,11] ,[6,13,9] , [2,12,100]])
print(S1)


# <b> General format </b>
# 
# <b> array_name[rows_fromat,columns_format] </b>
# 
# rows_fromat = [start,end,step]
# columns_format = [start,end,step]

# In[92]:


# get elements 9 and 100
# 9 is in  row index 1 and 100 is in row index 2
# 9 is in  column index 2 and 100 is in column index 2

print(S1[1,2])
print(S1[2,2])


# In[95]:


# starting index of row is 1 and ending index is 3 as exclusive , starting index of column is 2 and ending is 3 
print(S1[1: 3: 1, 2: 3: 1])


# In[99]:


# get [6,13] and [2,12]
print(S1[1: 3: 1 , 0: 2: 1])


# # Three Dimentional Array

# <b> General format </b>
# 
#  <b> i, j ,k </b>
#  
# <b> array_name[matrix_format, rows_fromat,columns_format] </b>
# 
# matrix_format = [start,end,step] 
# 
# rows_fromat = [start,end,step] 
# 
# columns_format = [start,end,step] 

# In[103]:


S2 =np.array( [[[1,2,3], [4,5,6]],[ [7,8,9], [10,11,12]]])
print(S2)
print(S2.shape)


# In[104]:


# slice first matrix
print(S2[0: 1, : :])


# In[107]:


oned = np.array([1,2,3,4,5,6,7])
print(oned[2:5])


# In[113]:


arr123 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr123[1:3,0:2])


# In[114]:


print(arr123[::2, ::-1])


# # Views vs Copy

# .Changes made to the view will affect the original array, whereas changes made to the copy will not affect the original array.
# 
# .View is just the view of original array, but copy is like creating new array

# In[117]:


view1 = np.array([10,20,30,40])
print(view1)


# In[118]:


view2 = view1.view()
view2[1] = 1000


# In[119]:


print(view1)


# In[120]:


print(view2)


# In[122]:


copy1 = np.array([10,20,30,40])
print(copy1)


# In[123]:


copy2= copy1.copy()
copy2[1] = 1000


# In[124]:


print(copy2)


# In[125]:


print(copy1)


# # Numpy Hstack Vs Vstack

# <b> Hstack is used to join two arrays Horizontally </b> 
# 
# <b> Vstack is used to join two arrays Vertically </b>

# In[128]:


a1 = np.array([1,2,3])
b1 = np.array([4,5,6])

print("a1 : {}" . format(a1))
print("dimension of a1 " , a1.ndim)

print("b1 : {}" . format(b1))
print("dimension of b1 " , b1.ndim)


# In[131]:


c1 = np.hstack((a1, b1))
               
print("c1: {}" . format(c1))
print("dimension of c1: " , c1.ndim)


# In[133]:


d1 = np.vstack((a1, b1))
               
print("d1: {}" . format(d1))
print("dimension of d1 :" , d1.ndim)


# In[134]:


A1=np.array([ [ 1,2],[3,4] ])
B1=np.array([ [ 5,2],[6,3] ])

C1 = np.vstack((A1, B1))
print(C1)


# In[139]:


M1=np.array([ [ 1,2],[3,4] ])
N1=np.array([ [ 5,6],[7,8] ])

D1 = np.hstack((M1, N1))
print(D1)


# # Numpy Concatenation

# In[151]:


con1 = np.array([[1,2] , [4,5]])
print(con1)
print(con1.shape)


# In[152]:


con2 = np.array([[7] , [8]])
print(con2)
print(con2.shape)


# In[153]:


con3 = np.array([[9,10]])
print(con3)
print(con3.shape)


# <b> Note </b> 
# 1. when axis = 0 , both concatenating arrays should have same number of columns(think like adding a new row) 
# 
# 2. when axis = 1 , both concatenating arrays should have same number of rows(think like adding a new column) 

# In[154]:


con4 = np.concatenate((con1,con3), axis = 0 )
print(con4)
print(con4.shape)


# In[155]:


con5 = np.concatenate((con1,con2), axis = 1 )
print(con5)
print(con5.shape)


# # Insert, Append and Delete

# In[156]:


app =np.array( [1,2,3,4])
print(app)


# In[158]:


#appending an element 45
np.append(app,45)


# In[159]:


# appending multiple values in to array
np.append(app, [ 100, 150,80])


# adding new row to a matrix

# In[160]:



Inr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(Inr)


# In[161]:


Inr1 = np.append(Inr , [[10,11,12]] , axis =0)
Inr1


# adding new column to a matrix

# In[163]:


Inr2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(Inr2)


# In[166]:


Inr3 = np.append(Inr2 , [[10],[11],[12]] , axis =1)
Inr3


# <b> Inserting in 2D array </b>

# In[167]:


Ins = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(Ins)


# In[169]:


np.insert(Ins, 1, [10,11,12] ,axis =0)


# <b> Deletion </b>

# In[175]:


del1 = np.array( [1,2,3,4])
print(del1)


# In[176]:


np.delete(del1 , 2)


# In[177]:


del2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(del2)


# In[179]:


# deleting 2nd row in in matix 
np.delete(del2, 1, axis=0)


# In[180]:


# deleting 2nd column in in matix 
np.delete(del2, 1, axis=1)


# In[ ]:




