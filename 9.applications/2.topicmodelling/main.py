# Importing Functions from helper files:
from packages import preprocessing, generateWordEmbedding, elbow, clusteriseAndGetTopics

##########################################################################################
# Data Preprocessing:

data = preprocessing.convertFileToVar('global_warming.txt') 
data = preprocessing.removespecialcharsAndNumbers(data)
data = preprocessing.tokenizeAndRemoveStopwordsAndSingleChar(data)
data = preprocessing.lemmatize(data)
lematized_list_cpy = data.copy()

#########################################################################################
# Generating Word-Vectors:

tokenizer, model = generateWordEmbedding.loadBERTModel()
data, X = generateWordEmbedding.getBERTVectors(data , model , tokenizer)
df = generateWordEmbedding.buildDFOfCurrentWordVectorRelation(data, X)
print(df.head())

#########################################################################################
# Getting No of clusters as 'k' in k-means clustering:

elbow_val = elbow.getElbowMethodGraph(X)
print("Elbow Value -> " + str(elbow_val))

#########################################################################################
# Clustering and getting top words as relevant topics:

km, y = clusteriseAndGetTopics.makeKClusters(elbow_val , X)
closest_overall_output_words , words_by_cluster_no , final_list_of_used_words , X , list_all_words = clusteriseAndGetTopics.getTopNounsFromEachCluster(km , data , X  , lematized_list_cpy , num_of_clusters = elbow_val)
topic_words , words_by_cluster_no, words_by_cluster_no_with_distances = clusteriseAndGetTopics.mergeNounsFromEachCluster(words_by_cluster_no , list_all_words)
print("Topics Obtained : \n" + str(set(topic_words)))

#########################################################################################
