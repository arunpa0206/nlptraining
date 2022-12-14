import matplotlib.pyplot as plt
import numpy as np

# evenly sampled time at 200ms
t = np.arange(0. , 5. , 0.2)

# red dashes, blue squares, green triangles
plt.plot(t,t, 'r--', t, t **2 , 'bs', t , t**3 , 'gh')
plt.show()