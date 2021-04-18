#!/usr/bin/env python
# coding: utf-8

# In[4]:


print("Je vais trouver un programme qui trouvera des numéros divisibles par 7 mais ne sont pas un multiple de 5 entre 2000 et 3200")
print("reponse de la premiere question")
LISTOFNUMBERS = [i for i in range(2000,3201) if i % 7==0 and i %5!=0]
print(LISTOFNUMBERS)


# In[5]:


def factorial(n):
    result = 1
    if n == 0:
        return result
    elif n > 0:
        for i in range(n,0,-1):
            result = result*i
    else:
        print("The given number is negative")
        result = None
    return result


# In[6]:


factorial(5)


# In[7]:


def dictGene(n):
    result = {}
    if n >=1:
        for i in range(1,n+1):
            result[i] = i*i
    return result


# In[8]:


dictGene(8)


# In[9]:


def missingChar(strr,pos):
    return strr[:pos] + strr[(pos+1):]


# In[10]:


missingChar('Kitten',4)


# In[14]:


import numpy as np


# In[15]:


def toList(array):
    return array.tolist()


# In[16]:


toList(np.array([[0,1],[2,3],[4,5]] ))


# In[17]:


def cov(array1,array2):
    return np.cov(array1,array2)


# In[18]:


array1 = np.array([0,1,2])
array2 = np.array([2,1,0])
cov(array1,array2)


# In[21]:


import math


# In[22]:


def sqRoot(D):
    C = 50
    H = 30
    return [int(math.sqrt((2*C*i)/H)) for i in D]


# In[23]:


sqRoot([100,150,180])


# In[ ]:




