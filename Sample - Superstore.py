#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[4]:


df=pd.read_excel('Sample - Superstore.xls')


# In[5]:


df.head()


# In[7]:


get_ipython().run_line_magic('matplotlib', 'inline')
import warnings
warnings.filterwarnings("ignore")


# In[8]:


pd.set_option("display.max_columns",100)
df.head()


# In[9]:


x=df['Discount']
y=df['Profit']

plt.scatter(x=x,y=y)


# In[13]:


df.groupby(['Region'])[['Profit']].mean()['Profit'].plot.bar()


# In[15]:


df.describe()


# In[16]:


df.isnull().sum()


# In[17]:


df.duplicated().sum()


# In[19]:


df.nunique()


# In[22]:


sns.scatterplot(x=df['Sales'], y=df['Quantity'], hue = df['Region'])


# In[28]:


plt.figure(figsize=(15,10))
sns.barplot(y=df['Sales'], x=df['Sub-Category'])
plt.xticks(rotation =90);
plt.title("sales by sub-category", fontname="Times New Roman",size=40)
plt.ylabel("Sales",size=20)
plt.xlabel("sub category", size=20);



# In[32]:


plt.figure(figsize=(15,10))
#fig=plt.figure()
plt.subplot(2,2,1)
sns.barplot(y=df['Sales'], x=df['Sub-Category'])
plt.xticks(rotation =90);
plt.title("sales by sub-category", fontname="Times New Roman",size=10)
plt.ylabel("Sales",size=10)
plt.xlabel("sub category", size=10);

plt.subplot(2,2,2)
sns.barplot(y=df['Sales'], x=df['Category'])
plt.xticks(rotation =90);
plt.title("sales by sub-category", fontname="Times New Roman",size=10)
plt.ylabel("Sales",size=10)
plt.xlabel("sub category", size=10);


# In[36]:


plt.figure(figsize=(15,10))
#fig=plt.figure()
plt.subplot(2,2,1)
sns.barplot(y=df['Sales'], x=df['Sub-Category'])
plt.xticks(rotation =90);
plt.title("sales by sub-category", fontname="Times New Roman",size=10)
plt.ylabel("Sales",size=10)
plt.xlabel("sub category", size=10)

plt.subplot(2,2,2)
sns.scatterplot(y=df['Sales'], x=df['Category'])
plt.xticks(rotation =90);
plt.title("sales by sub-category", fontname="Times New Roman",size=10)
plt.ylabel("Sales",size=10)
plt.xlabel("sub category", size=10)

plt.subplot(2,2,3)
sns.barplot(y=df['Sales'], x=df['Category'])
plt.xticks(rotation =90);
plt.title("sales by sub-category", fontname="Times New Roman",size=10)
plt.ylabel("Sales",size=10)
plt.xlabel("sub category", size=10)

plt.subplot(2,2,4)
sns.barplot(y=df['Sales'], x=df['Category'])
plt.xticks(rotation =90);
plt.title("sales by sub-category", fontname="Times New Roman",size=10)
plt.ylabel("Sales",size=10)
plt.xlabel("sub category", size=10)



# In[44]:


plots_to_create =['Sub-Category','Category']


fig=plt.figure()

for i,j in enumerate(plots_to_create):
    plt.subplot(2,2,i+1)
    sns.barplot(y=df['Sales'], x=df[j])
    plt.xticks(rotation =90);
    plt.title("sales by sub-category", fontname="Times New Roman",size=10)
    plt.ylabel("Sales",size=10)
    plt.xlabel("sub category", size=10)





# In[ ]:




