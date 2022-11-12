#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
import sagemaker
from sagemaker import get_execution_role
import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt


# In[7]:


# consider X as height of a person in metres.
train_data_X = np.linspace(-1, 1, 100)
# consider Y as weight of a person in kg calulated by taking ideal BMI
train_data_Y = 4 * train_data_X + np.random.randn(100) * 0.44


# In[8]:


print(train_data_X)


# In[9]:


print(train_data_Y)


# In[6]:


plt.scatter(train_data_X, train_data_Y, label='data', color=['blue'])


# In[10]:


from keras.models import Sequential
from keras.layers import Dense
model = Sequential()


# In[11]:


model.add(Dense(kernel_initializer="uniform", activation="linear", input_dim=1, units=1))


# In[12]:


model.summary()


# In[14]:


result = model.predict(train_data_X)


# In[13]:


model.compile(optimizer='sgd', loss='mse')
model.fit(train_data_X, train_data_Y, epochs=2500, batch_size=10)


# In[15]:


plt.scatter(train_data_X, train_data_Y, label='data', color=['red'])
plt.plot(train_data_X, result, label='prediction')
plt.legend()
plt.show()


# In[16]:


model.save('model.h5')


# In[17]:


import sagemaker
s3_path_to_data = sagemaker.Session().upload_data(bucket='sentimentanalysis-s3bucket', 
                                                  path='model.h5', 
                                                  key_prefix='my_model')


# In[ ]:




