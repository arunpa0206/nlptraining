###########################################################################################################

def termFrequency(term, doc):
     
    """
    Input: term: Term in the Document, doc: Document
    Return: Normalized tf: Number of times term occurs
      in document/Total number of terms in the document
    """
    # Splitting the document into individual terms
    normalizeTermFreq = doc.lower().split()
 
    # Number of times the term occurs in the document
    term_in_document = normalizeTermFreq.count(term.lower())
 
    # Total number of terms in the document
    len_of_document = float(len(normalizeTermFreq ))
 
    # Normalized Term Frequency
    normalized_tf = term_in_document / len_of_document
 
    return normalized_tf

###########################################################################################################

def inverseDocumentFrequency(term, allDocs):
    import math
    num_docs_with_given_term = 0

    """
    Input: term: Term in the Document,
    allDocs: List of all documents
    Return: Inverse Document Frequency (idf) for term
    = Logarithm ((Total Number of Documents) /
    (Number of documents containing the term))
    """
    # Iterate through all the documents
    for doc in allDocs:
        
        """
        Putting a check if a term appears in a document.
        If term is present in the document, then
        increment "num_docs_with_given_term" variable
        """
        if term.lower() in doc.lower().split():
            num_docs_with_given_term += 1

    if num_docs_with_given_term > 0:
        # Total number of documents
        total_num_docs = len(allDocs)

        # Calculating the IDF
        idf_val = math.log(float(total_num_docs) / num_docs_with_given_term)
        return idf_val
    else:
        return 0

#########################################################################################################

# All preprocessing done.
doc_list = ['ben study computer computer lab', 'steve teach brown university', 'data scientist work large dataset']

tf_idf_1 = []
tf_idf_2 = []

# Specifying Query Terms
word_1 = 'data'
word_2 = 'scientist'

for doc in doc_list:
    tf_1 = termFrequency(word_1, doc)
    idf_1 = inverseDocumentFrequency(word_1, doc_list)
    tf_idf_1.append(tf_1 * idf_1) 

    tf_2 = termFrequency(word_2, doc)
    idf_2 = inverseDocumentFrequency(word_2, doc_list)
    tf_idf_2.append(tf_2 * idf_2) 

print('Doc-1 Doc-2       Doc-3')
print(str(tf_idf_1) + "  ->  " + word_1)
print(str(tf_idf_2) + "  ->  " + word_2)

# So Doc-3 is best result for 'data scientist' query.

############################################################################################################

