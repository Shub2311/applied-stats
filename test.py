#!/usr/bin/env python
# coding: utf-8

# In[3]:


import scipy
from scipy import stats
import pandas as pd


# In[5]:


df = {'observe': [41,70],'expected': [33,67]}
df1 = pd.DataFrame(df)


# In[6]:


df1


# In[7]:


df1['dev'] = df1['observe']-df1['expected']


# In[8]:


chi = sum((df1['dev']**2)/df1['expected'])


# In[9]:


p_value = scipy.stats.chi2.ppf(0.5,1)


# In[10]:


if p_value < 0.05:
    print('P value is' , p_value)
    print()
    print('since p is less than alpha we reject the null hypothesis')
else:
    print('p value is', p_value)
    print()
    print('since p is more than alpha, we ccept the null hypothesis')


# In[ ]:




