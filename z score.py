#!/usr/bin/env python
# coding: utf-8

# In[22]:


from numpy import random

x = random.normal(size=(10, 2))

print(x)


# In[23]:


import pandas as pd
df = pd.DataFrame(data=x)
df.to_csv('data.csv')
deee = pd.read_csv('data.csv')
deee


# In[24]:


mean = sum(x) / len(x)
differences = [(x - mean)**2 for i in x]
sum_of_differences = sum(differences)
standard_deviation = (sum_of_differences / (len(x) - 1)) ** 0.5

print(standard_deviation)


# In[25]:


# Calculate the z-score from scratch
zscores = [(x - mean) / standard_deviation for value in x]

print(zscores)


# In[ ]:




