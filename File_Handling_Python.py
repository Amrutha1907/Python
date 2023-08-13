#!/usr/bin/env python
# coding: utf-8

# # File Handling

# Allows to create, update,read and update files along with other handling options.
# 
# The <b> os </b> module provides functions for interacting with the operating systems.<b> OS </b> is under python's standard utility modules.

# In[1]:


import os


# In[2]:


# cwd- current working directory
os.getcwd()


# In[3]:


# change the cwd
os.chdir("C:\DSA\CML\Data Files")
os.getcwd()


# In[4]:


# listing the current working directory
os.listdir("C:\DSA\CML\Data Files")


# <b> Creating New Directory </b>

# There are two ways <b> os.mkdir() </b> and <b> os.makedirs() </b>

# <b> os.mkdir() </b>
# is used to create a new directory named path with the specified numeric mode.This method raises fileExixtserror if the directory already exisxt.

# In[5]:


# New Directory
directory = "demo1"

# parent Directory
parent_dir = "C:/DSA/CML/Directory/"

# path
path=os.path.join(parent_dir, directory)


os.mkdir(path)
print("directory '%s' created " % directory)



# New Directory
directory = "demo2"

# parent Directory
parent_dir = "C:/DSA/CML/Directory/"

# mode
mode = 0o666

# path
path=os.path.join(parent_dir, directory)


os.mkdir(path , mode)
print("directory  '%s' created " % directory)


# <b> os.makedirs() </b> : used to create directory recursively.That means while making leaf directory if any intermediate level directory is missing,
#     os.makedirs() will cretae them all.

# In[6]:


# New Directory
directory = "demo5"

# parent Directory
parent_dir = "C:/DSA/CML/Directory/demo3/demo4/"


# path
path=os.path.join(parent_dir, directory)


os.makedirs(path)
print("directory  '%s' created " % directory)


# <b> Deleting Directory?/Files </b>

# <b>1.os.remove() </b> 
# 
# <b>2.os.rmdir() </b>

# In <b> os.remove() </b>  can rmoev or delete a file path.This method can not remove or delete the directory

# In[7]:


# file name
file = "movies-db-1.csv"

# file location
location = "C:/DSA/CML/Directory/demo7/"

# path
path = os.path.join(location, file)

os.remove(path)


# In <b> os.rmdir() </b> can rmoev or delete an empty directory .It will be raised if the specified path is not an empty directory

# In[8]:


# file name
file = "demo1"

# file location
location = "C:/DSA/CML/Directory/"

# path
path = os.path.join(location, file)

os.rmdir(path)


# # FILES

# In[9]:


pwd


# <b> Creating a File </b>

# In[12]:


get_ipython().run_cell_magic('writefile', 'text.txt', 'first line\nsecond line\nthird line\nfourth line')


# In[17]:


os.listdir('C:\\DSA\\CML\\Data Files\\')


# In[19]:


filepath = open ("C:\\DSA\\CML\\Data Files\\text.txt")
filepath


# <b> .read() and .seek() </b>

# In[20]:


filepath.read()


# In[21]:


filepath.seek(0)
print(filepath.read())


# <b> Readlines </b>

# For reading the files line by line

# In[23]:


filepath.seek(0)
print(filepath.readlines())


# In[24]:


# for closing the file
filepath.close()


# <b> Writing to File </b>

# In[26]:


writefile =open ("C:\\DSA\\CML\\Data Files\\text.txt" , 'w+')


# In[27]:


writefile.write("the new first line")


# In[28]:


writefile.seek(0)
writefile.read()


# <b> writelines </b>

# In[37]:


with open ('newtextfile.txt' , 'w+') as f:
    lines=['python is a programming language']
    f.writelines(lines)


# In[38]:


# read file
with open ('newtextfile.txt' , 'r') as f:
    lines = f.readlines()
print(lines)


# <b> Appending to file </b>

# In[39]:


myfile = open('text.txt' , 'a+')
myfile.write('The new second line appended')
myfile.write('The new third line appended')
myfile.seek(0)
myfile.read()


# In[40]:


myfile.seek(0)
print(myfile.read())


# In[41]:


myfile.close()


# In[ ]:




