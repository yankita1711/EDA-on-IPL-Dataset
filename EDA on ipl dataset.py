#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns


# In[2]:


ipl=pd.read_csv('matches.csv')


# In[3]:


ipl.head()


# In[5]:


ipl.shape


# In[6]:


ipl['player_of_match'].value_counts()


# In[7]:


ipl['player_of_match'].value_counts()[0:10]


# In[8]:


ipl['player_of_match'].value_counts()[0:5]


# In[10]:


list(ipl['player_of_match'].value_counts()[0:5].keys())


# In[11]:


plt.figure(figsize=(8,5))
plt.bar(list(ipl['player_of_match'].value_counts()[0:5].keys()),list(ipl['player_of_match'].value_counts()[0:5]),color="g")
plt.show()


# In[12]:


list(ipl['player_of_match'].value_counts()[0:5].keys())


# In[ ]:




