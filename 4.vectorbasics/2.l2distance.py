import numpy as np
from sklearn.metrics.pairwise import euclidean_distances

points = np.asarray([[1,2,3.5],[4,1,2],[0,0,2],[3.4,1,5.6]]) 
dist_mat = euclidean_distances(points,points) 

print(dist_mat)