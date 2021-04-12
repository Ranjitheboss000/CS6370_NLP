from util import *

# Add your import statements here
import numpy as np
from numpy import dot
from numpy.linalg import norm
import operator

class InformationRetrieval():

    def __init__(self):
        self.index = None



    def buildIndex(self, docs, docIDs):
        """
        Builds the document index in terms of the document
        IDs and stores it in the 'index' class variable

        Parameters
        ----------
        arg1 : list
            A list of lists of lists where each sub-list is
            a document and each sub-sub-list is a sentence of the document
        arg2 : list
            A list of integers denoting IDs of the documents
        Returns
        -------
        None
        """

        types = []
        D = len(docs)

        for doc in docs:
            for sentence in doc:
                for word in sentence:
                    if word not in types:
                        types.append(word)

        L = len(types)   
        self.types = types # storing types of the input dataset as a class variable

        TD_matrix = np.zeros([L,D]) # term-document matrix
                                    # At the end
                                    # each column of this matrix will be the TD-IDF vector representation of the corresponding document


        for col, doc in enumerate(docs):                  # iterating over documents
            for sentence in doc:                          # iterating over sentences in a document
                for word in sentence:
                    row = types.index(word)
                    TD_matrix[row,col] += 1

        df = np.sum(TD_matrix > 0, axis=1)     # sum across rows over the Boolean matrix
                                               # document frequency for each type in cranfield dataset 

        self.IDF = np.log(D/df)

        for i in range(L):
            TD_matrix[i,:] *= self.IDF[i]   

        # Dictionary in which key:value ==> doc_ID:Corresponding TD-IDF vector representation
        index = {doc_id:vector for (doc_id,vector) in zip(docIDs,TD_matrix.transpose())}  

        self.index = index


    def rank(self, queries):
        """
        Rank the documents according to relevance for each query

        Parameters
        ----------
        arg1 : list
            A list of lists of lists where each sub-list is a query and
            each sub-sub-list is a sentence of the query


        Returns
        -------
        list
            A list of lists of integers where the ith sub-list is a list of IDs
            of documents in their predicted order of relevance to the ith query
        """

        doc_IDs_ordered = []
        L = len(self.types)

        TQ_matrix = np.zeros([L,len(queries)]) 


        for row, typ in enumerate(self.types):
            for col, query in enumerate(queries):       # iterating over queries
                for sentence in query:                  # iterating over sentences in a query
                    for word in sentence:               # iterating over word in a sentence of a query
                        if typ == word: 
                            TQ_matrix[row,col] += 1 

        for i in range(L):
            TQ_matrix[i,:] = self.IDF[i]*TQ_matrix[i,:]    


        doc_IDs_ordered  = []

        for j in range(len(queries)):
            cosine_similarity = {}
            for doc_id, doc_vector in self.index.items():
                x,y = doc_vector, TQ_matrix[:,j]
                cosine_similarity[doc_id] = dot(x,y)/(norm(x)*norm(y)) 
                # In the above dictionary, key:value ==> document ID:Its cosine similarity with (j+1)th query

            # Desired sublist of "doc_IDs_ordered" is obtained by sorting cosine_similarity in descending order 
            # ie., decreasing order of closeness of documents with (j+1)th query 
            # Followed by appending it to the doc_IDs_ordered

            doc_IDs_ordered.append([x for x, _ in sorted(cosine_similarity.items(),key = operator.itemgetter(1),reverse = True)])

        return doc_IDs_ordered




