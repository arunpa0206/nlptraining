import numpy as np
import pandas as pd
data = [{'a': 1, 'b': 2}, {'a': 1, 'b': 2, 'c': 3.0}]
df = pd.DataFrame(data, index=['first', 'second'])

print(df)