#!/usr/bin/env python
# coding: utf-8

# In[1]:



get_ipython().run_line_magic('pylab', 'inline')
import numpy as np


# In[26]:


#### We start with positive weights that don't sum to 1
P=np.array([[2.,5,4],[1,1,2]])
P2=copy(P)
P


# In[27]:


# We then normalize the weights
# using Pure Python

#Compute the sum
s=0
for i in range(shape(P)[0]):
    for j in range(shape(P)[1]):
        s+=P[i,j]
print('the sum is ',s)
#divide by the sum
for i in range(shape(P)[0]):
    for j in range(shape(P)[1]):
        P[i,j] /= s
P


# In[28]:


# Using Numpy we can write it in a much shorter way
P2/=sum(P2)
P2


# In[29]:


# The values that the random variables x and y take
x=np.array([1,2,6])
y=np.array([-3,3])


# In[30]:


# The pure python way
Px=[0.]*shape(P)[1]
Py=[0.]*shape(P)[0]

for i in range(len(Px)):
    for j in range(len(Py)):
        Px[i]+=P[j,i]
        Py[j]+=P[j,i]
Px,Py


# In[31]:


#the numpy way:
Px=sum(P,axis=0)
Py=sum(P,axis=1)
Px,Py


# In[32]:


# The pure python way
for i in range(len(Px)):
    for j in range(len(Py)):
        if Px[i]*Py[j] != P[j,i]:
            print("Px[%d]*Py[%d] != P[%d,%d] ::::: %5.3f*%5.3f = %5.3f != %5.3f"%(i,j,j,i,Px[i],Py[j],Px[i]*Py[j],P[j,i]))


# In[33]:


# The numpy way
np.outer(Px,Py).T - P


# In[34]:


from math import sqrt
#The python way
Ex = 0
for i in range(3):
    Ex+=Px[i]*x[i]
Ey = 0
for i in range(2):
    Ey+=Py[i]*y[i]

varx = 0
for i in range(3):
    varx+=Px[i]*(x[i] - Ex)**2
stdx = sqrt(varx)

vary = 0
for i in range(2):
    vary+=Py[i]*(y[i] - Ey)**2
stdy = sqrt(vary)

Ex,Ey,stdx,stdy


# In[35]:


# In numpy you can use np.dot(A,B) which calculates the pairwise product of elements in A and B
# and sums them up
Ex=np.dot(Px,x)
Ey=np.dot(Py,y)
Ex2=np.dot(Px,x**2)
Ey2=np.dot(Py,y**2)
stdx=sqrt(Ex2-Ex**2)
stdy=sqrt(Ey2-Ey**2)
print('Ex=%f,Ey=%f,stdx=%f,stdy=%f'%(Ex,Ey,stdx,stdy))


# In[36]:


nx=x-Ex
nx


# In[38]:


ny=y-Ey
ny


# In[39]:


# in python
s=0
for i in range(len(x)):
    for j in range(len(y)):
        s+=P[j,i]*nx[i]*ny[j]
print('the covariance is',s) #our expected values are now 0 so nothing to subtract


# In[40]:


# numpy

print('the covariance is', np.dot(P.flatten(), np.outer(ny,nx).flatten()))


# In[42]:


import math
# Finding the variance is essential before calculating the standard deviation
def varinc(val, ddof=0):
    n = len(val)
    m = sum(val) / n
    return sum((x - m) ** 2 for x in val) / (n - ddof)
# finding the standard deviation
def stddev(val):
    vari = varinc(val)
    stdev = math.sqrt(vari)
    return stdev

print(stddev([5, 9, 6, 2, 6, 3, 7, 4, 8, 6]))


# In[ ]:




