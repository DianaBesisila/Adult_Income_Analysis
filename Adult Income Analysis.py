#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[5]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


pd.read_csv(r"C:\Users\DIANA\Downloads\adult.csv")


# In[4]:


df=pd.read_csv(r"C:\Users\DIANA\Downloads\adult.csv")
df


# # Display Top 10 rows in the dataset

# In[6]:


df.head(10)


# # Display Lasst 10 rows in the dataset

# In[7]:


df.tail(10)


# # Checking the Shape of the Dataset (Number of rows and Columns)

# In[8]:


df.shape


# In[9]:


print('number of rows',df.shape[0])
print('number of columns',df.shape[1])


# # To Get information of the Dataset

# In[10]:


df.info()


# # To fetch random sample(50%) from our Dataset

# In[11]:


df.sample(frac=0.50)


# # To fetch random sample(50%) from our Dataset (Same sequence of the random Data)

# In[20]:


df1=df.sample(frac=0.50,random_state=100)
df1


# # Checking null Values and sum of the null values

# In[21]:


df.isnull().sum()


# In[22]:


sns.heatmap(df.isnull())


# # Perfoming Data Cleaning replace [?] with NaN

# In[24]:


df.isnull().sum()


# In[26]:


df.isin(['?']).sum()


# In[27]:


import numpy as np


# In[28]:


df.columns


# In[31]:


df['workclass']=df['workclass'].replace('?',np.nan)
df['occupation']=df['occupation'].replace('?',np.nan)
df['native-country']=df['native-country'].replace('?',np.nan)


# In[32]:


df.isin(['?']).sum()


# In[33]:


df.isnull().sum()


# In[34]:


sns.heatmap(df.isnull())


# # Drop all the missing Value

# In[35]:


df.dropna(how='any',inplace=True)


# In[36]:


df.isnull().sum()


# In[38]:


df.shape


# In[39]:


48842-45222


# # Check for  Duplicates Data and Drop them

# In[41]:


dup=df.duplicated().any()


# In[45]:


print('are there any duplicates values in dataset?',dup)


# In[46]:


df=df.drop_duplicates()


# In[48]:


df.shape


# # To get Overall Statics about the Data Frame

# In[49]:


df.describe()


# In[50]:


df.describe(include='all')


# In[52]:


df.columns


# # To drop the following columns 'educational-num','capital-gain','capital-loss'

# In[55]:


df=df.drop(['educational-num','capital-gain','capital-loss'],axis=1)


# In[56]:


df.columns


# # Univariate Analysis
# 

# # To find the Distribution of the Age Column

# In[57]:


df['age'].describe()


# In[59]:


df['age'].hist()


# # Find total number of Persons Having age Between 17 to 48 (Inclusive) using Between method.

# In[67]:


sum((df['age']>=17) & (df['age']<=18))


# In[69]:


sum(df['age'].between(17,18))


# # To find the distribution of Workclass column

# In[70]:


df.columns


# In[73]:


plt.figure(figsize=(10,10))
df['workclass'].hist()


# # How many have Bahelors or Masters Degree?

# In[72]:


df['workclass'].describe()


# In[75]:


df.columns


# In[81]:


df['education'].head(20)


# In[86]:


df['education'].isin(['Bachelors','Masters'])


# In[87]:


sum(df['education'].isin(['Bachelors','Masters']))


# # Bivariate Analysis

# # It is used to find relationship between two variables

# In[94]:


df.columns


# In[105]:


sns.boxplot(x='income',y='age',data=df)


# # Replace Income values with ['<=50k','>=50k'] with 0 and 1

# In[106]:


df.columns


# In[110]:


df['income'].unique()


# In[111]:


df['income'].value_counts()


# In[131]:


sns.countplot(x='income',data=df)


# In[135]:


df.replace(to_replace=['<=50K', '>50K'], value=[0, 1], inplace=True)


# In[136]:


df.head()


# # Which WorkClass is getting High Income?

# In[138]:


df.groupby('workclass')['income'].mean().sort_values(ascending=False)


# # Who has better Chance to get salary greater than 50k? is it male or female?

# In[141]:


df.groupby('gender')['income'].mean().sort_values(ascending=False)


# # Convert work class column data type to category data type

# In[142]:


df.info()


# In[144]:


df['workclass'].astype('category')


# In[146]:


df['workclass']=df['workclass'].astype('category')


# In[147]:


df.info()


# In[ ]:




