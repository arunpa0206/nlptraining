#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import sagemaker
from sagemaker import get_execution_role
import tensorflow as tf
from tensorflow import keras


# In[2]:


import numpy as np
import matplotlib.pyplot as plt
train_data_X = np.linspace(-1, 1, 100)


# In[3]:


# y = 4 * x + random values
train_data_Y = 4 * train_data_X + np.random.randn(100) * 0.44


# In[4]:


train_data_X


# In[5]:


train_data_Y


# In[6]:


plt.scatter(train_data_X, train_data_Y, label='data', color=['blue'])


# In[7]:


from keras.models import Sequential
from keras.layers import Dense
model = Sequential()


# In[8]:


model.add(Dense(kernel_initializer="uniform", activation="linear", input_dim=1, units=1))


# In[9]:


model.summary()


# In[10]:


result = model.predict(train_data_X)


# In[11]:


plt.scatter(train_data_X, train_data_Y, label='data', color=['red'])
plt.plot(train_data_X, result, label='prediction')
plt.legend()
plt.show()


# In[12]:


model.compile(optimizer='sgd', loss='mse')
model.fit(train_data_X, train_data_Y, epochs=5, batch_size=10)


# In[14]:


model.save('model.h5')


# In[16]:


import sagemaker
s3_path_to_data = sagemaker.Session().upload_data(bucket='sentimentanalysis-s3bucket', 
                                                  path='model.h5', 
                                                  key_prefix='my_model')


# In[ ]:




