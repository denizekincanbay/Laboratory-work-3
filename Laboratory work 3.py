#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# In[2]:


salesDist = pd.read_csv(r'C:\Users\ekinc\Downloads\stores-dist.csv')
salesDist.head()


# In[3]:


salesDist = salesDist.rename(columns={'annual net sales':'sales','number of stores in district':'stores'})
salesDist.head()


# In[4]:


salesDist.corr()


# In[7]:


sales = salesDist.drop(columns=["district"], axis = 1)

sales.head()


# In[9]:


y = sales['sales']
x = sales.stores


# In[10]:


get_ipython().run_line_magic('matplotlib', 'inline')

plt.figure(figsize=(20,10))

plt.plot(x,y, 'o', markersize = 15)

plt.ylabel('Annual Net Sales', fontsize = 30)
plt.xlabel('Number of Stores in the District', fontsize = 30)

plt.xticks(fontsize = 20)
plt.yticks(fontsize = 20)

plt.show()


# In[12]:


m, b = np.polyfit(x,y,1) 
print ('The slope of line is {:.2f}.'.format(m))
print ('The y-intercept is {:.2f}.'.format(b))
print ('The best fit simple linear regression line is {:.2f}x + {:.2f}.'.format(m,b))


# In[13]:


y_mean = y.mean()    
x_mean = x.mean()
print ('The centroid for this dataset is x = {:.2f} and y = {:.2f}.'.format(x_mean, y_mean))


# In[14]:


get_ipython().run_line_magic('matplotlib', 'inline')

plt.figure(figsize=(20,10))

plt.plot(x,y, 'o', markersize = 14, label = "Annual Net Sales") 

plt.plot(x_mean,y_mean, '*', markersize = 30, color = "r") 

plt.plot(x, m*x + b, '-', label = 'Simple Linear Regression Line', linewidth = 4)

plt.ylabel('Annual Net Sales', fontsize = 30)
plt.xlabel('Number of Stores in District', fontsize = 30)

plt.xticks(fontsize = 20)
plt.yticks(fontsize = 20)

plt.annotate('Centroid', xy=(x_mean-0.1, y_mean-5), xytext=(x_mean-3, y_mean-20), arrowprops=dict(facecolor='black', shrink=0.05), fontsize = 30)

plt.legend(loc = 'upper right', fontsize = 20)


# In[15]:


def predict(query):
    if query >= 1:
        predict = m * query + b
        return predict
    else:
        print ("You must have at least 1 store in the district to predict the annual net sales.")


# In[16]:


predict(4)


# In[ ]:




