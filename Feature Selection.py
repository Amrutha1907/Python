#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# # UNIVARIATE SELECTION
# 
# 
# 

# Statistical tests can be used to select those features that are strongly related to the dependent features.

# In[2]:


pip install scipy


# In[3]:


from sklearn.feature_selection import SelectKBest 
from sklearn.feature_selection import chi2


# In[4]:


#reading the dataset
df=pd.read_csv(r'C:\DSA\CML\Data Files\mobile.csv')
df.head()


# In[12]:


# number of unique values
df.nunique().price_range 


# In[13]:


# unique values
df.price_range.unique()


# In[19]:


# Independent Features
X= df.iloc[:,0:20]
# Dependent Features
y= df.iloc[:,-1]


# In[23]:


# apply SelectKBest class to extract top 10 best features
bestfeatures = SelectKBest(score_func=chi2, k=10)
fit = bestfeatures.fit(X,y)


# In[24]:


feature_scores = pd.concat([pd.DataFrame(X.columns), pd.DataFrame(fit.scores_)], axis = 1)
feature_scores.columns = ["feature", "score"]
feature_scores.sort_values(by="score", ascending=False)


# In[25]:


feature_scores.nlargest(10, "score")


# ## Feature Importance
#  We can get the feature importance of our dataset using the feature_importance_ property of our model.

# In[27]:


from sklearn.ensemble import ExtraTreesClassifier
model = ExtraTreesClassifier()
model.fit(X,y)


# In[28]:


print(model.feature_importances_)


# In[29]:


plt.figure(figsize=(14,8))
plt.barh(X.columns, model.feature_importances_)
plt.title("Feature Importances")
plt.show()


# ## Correlation Matrix

# In[32]:


correlation_matrix = df.corr()
correlation_matrix


# In[33]:


plt.figure(figsize=(18,12))
sns.heatmap(correlation_matrix, center=0, annot=True)
plt.show()


# In[34]:


diabetes = pd.read_csv("C:\DSA\CML\Data Files\diabetes.csv")
#print the head 
diabetes.head()


# In[38]:


diabetes.isnull().sum()


# In[ ]:




