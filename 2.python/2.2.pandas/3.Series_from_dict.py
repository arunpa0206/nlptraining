import numpy as np
import pandas as pd

data = {'a': 0,'b': 1,'c': 2,'d': 3}
s = pd.Series(data)
print(s)

#############################################
print('-------------------------')

data = {'a': 0,'b': 1,'c': 2,'d': 3}
#Specify the keys that should be included through indexing
s = pd.Series(data, index=['b','c','d','e'])
print(s)