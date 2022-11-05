import numpy as np

# Function that takes two python lists as vectors and returns cosine-similarity:
def CosineSimilarity(vec_1, vec_2):
    vA = np.asarray(vec_1)
    vB = np.asarray(vec_2)

    print("First-vector :  " + str(vA))  
    print("Second-vector :  " + str(vB))
    print('-----------------------------------------------')

    cos_sim = np.dot(vA, vB) / (np.sqrt(np.dot(vA,vA)) * np.sqrt(np.dot(vB,vB)))
    return cos_sim


#(Case-1) Two vectors are nearly similar:
vec_1 = [0.112, -2.11, 5.23, -8.93,]
vec_2 = [0.970, -1.41, 4.87, -6.67,]
#(Case-2) Two vectors are far-away(Nearly-Orthogonal):
vec_3 = [0.112, -2.11, 5.23, -8.93,]
vec_4 = [-19.3, 1.51, -1.87, -2.67,]
#(Case-3) Two vectors are opposite:
vec_5 = [0.112, -2.11, 5.23, -8.93,]
vec_6 = [-0.112, 2.11, -5.23, 8.93,]

# Calculating cosine-similarity for both cases:
cos_sim_1 = CosineSimilarity(vec_1, vec_2)
cos_sim_2 = CosineSimilarity(vec_3, vec_4)
cos_sim_3 = CosineSimilarity(vec_5, vec_6)

# Printing Results:
print("\nCosine-Similarity Case-1 : " + str(cos_sim_1))
print("Cosine-Similarity Case-2 : " + str(cos_sim_2))
print("Cosine-Similarity Case-3 : " + str(cos_sim_3))
