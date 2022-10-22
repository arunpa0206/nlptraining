import pandas as pd

#Create and empty series:
s = pd.Series(dtype='float64')
print(s)

#Series without index:
import numpy as np
import pandas as pd

data = np.array(['a','b','c','d'])
s = pd.Series(data)
print(s)