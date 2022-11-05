import keras
from keras.models import Sequential
from keras.layers import Dense, Activation
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

#height of 200 people between 1 to 6 feet
height = data  = np.linspace(1,6,200)
#randomly generate weight
weight = height*4 + np.random.randn(*height.shape) * 0.3


model = Sequential()
#input = height  and output =weight
model.add(Dense(1, input_dim=1, activation='linear'))

model.compile(optimizer='sgd', loss='mse', metrics=['mse'])

model.fit(height,weight, batch_size=1, epochs=30, shuffle=False)

predict = model.predict(data)
print(predict)

