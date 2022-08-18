#!/usr/bin/env python
# coding: utf-8

# In[3]:


from numpy import random

x = random.normal(size=(100, 5))

print(x)


# In[12]:


import pandas as pd
df = pd.DataFrame(data=x)
df.to_csv('data.csv')
deee = pd.read_csv('data.csv')
deee


# In[ ]:


aa

