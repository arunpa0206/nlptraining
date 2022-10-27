# Importing Functions from helper files:
from packages import _1_preprocessing, _2_generateWordEmbedding, _3_elbow, _4_clusteriseAndGetTopics

##########################################################################################
# Data Preprocessing:

data = _1_preprocessing.convertFileToVar('global_warming.txt') 
data = _1_preprocessing.removespecialcharsAndNumbers(data)
data = _1_preprocessing.tokenizeAndRemoveStopwordsAndSingleChar(data)
data = _1_preprocessing.lemmatize(data)
lematized_list_cpy = data.copy()

#########################################################################################
# Generating Word-Vectors:

tokenizer, model = _2_generateWordEmbedding.loadBERTModel()
data, X = _2_generateWordEmbedding.getBERTVectors(data , model , tokenizer)
df = _2_generateWordEmbedding.buildDFOfCurrentWordVectorRelation(data, X)
print(df.head())

#########################################################################################
# Getting No of clusters as 'k' in k-means clustering:

elbow_val = _3_elbow.getElbowMethodGraph(X)
print("Elbow Value -> " + str(elbow_val))

#########################################################################################
# Clustering and getting top words as relevant topics:

km, y = _4_clusteriseAndGetTopics.makeKClusters(elbow_val , X)
closest_overall_output_words , words_by_cluster_no , final_list_of_used_words , X , list_all_words = _4_clusteriseAndGetTopics.getTopNounsFromEachCluster(km , data , X  , lematized_list_cpy , num_of_clusters = elbow_val)
topic_words , words_by_cluster_no, words_by_cluster_no_with_distances = _4_clusteriseAndGetTopics.mergeNounsFromEachCluster(words_by_cluster_no , list_all_words)
print("Topics Obtained : \n" + str(topic_words))

#########################################################################################