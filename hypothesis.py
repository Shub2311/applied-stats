#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


BeforeCourse = [44,40,61,52,32,44,70,41,67,72,53,72]
AfterCourse = [53,38,69,57,46,39,73,48,73,74,60,78]


# In[3]:


a = np.array(BeforeCourse)
b = np.array(AfterCourse)


# In[4]:


print(np.var(a),np.var(b))


# In[5]:


import scipy.stats as stats


# In[6]:


stats.ttest_ind(a,b,equal_var= True)


# In[ ]:




