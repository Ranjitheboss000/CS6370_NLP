from util import *

# Add your import statements here
from math import log2


class Evaluation():
    
    def __init__(self):
        self.ground_truth = None
    
    def queryPrecision(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
        """
        Computation of precision of the Information Retrieval System
        at a given value of k for a single query

        Parameters
        ----------
        arg1 : list
            A list of integers denoting the IDs of documents in
            their predicted order of relevance to a query
        arg2 : int
            The ID of the query in question
        arg3 : list
            The list of IDs of documents relevant to the query (ground truth)
        arg4 : int
            The k value

        Returns
        -------
        float
            The precision value as a number between 0 and 1
        """

        precision = len(set(query_doc_IDs_ordered[:k]) & set(true_doc_IDs))/k

        return precision


    def meanPrecision(self, doc_IDs_ordered, query_ids, qrels, k):
        """
        Computation of precision of the Information Retrieval System
        at a given value of k, averaged over all the queries

        Parameters
        ----------
        arg1 : list
            A list of lists of integers where the ith sub-list is a list of IDs
            of documents in their predicted order of relevance to the ith query
        arg2 : list
            A list of IDs of the queries for which the documents are ordered
        arg3 : list
            A list of dictionaries containing document-relevance
            judgements - Refer cran_qrels.json for the structure of each
            dictionary
        arg4 : int
            The k value

        Returns
        -------
        float
            The mean precision value as a number between 0 and 1
        """

        meanPrecision = 0

        for i in range(len(query_ids)):
            true_doc_IDs = [int(dic["id"]) for dic in qrels if dic["query_num"] == str(query_ids[i])]
            meanPrecision += self.queryPrecision(doc_IDs_ordered[i], query_ids[i],true_doc_IDs, k)

        meanPrecision = meanPrecision/len(query_ids)

        #Fill in code here

        return meanPrecision


    def queryRecall(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
        """
        Computation of recall of the Information Retrieval System
        at a given value of k for a single query

        Parameters
        ----------
        arg1 : list
            A list of integers denoting the IDs of documents in
            their predicted order of relevance to a query
        arg2 : int
            The ID of the query in question
        arg3 : list
            The list of IDs of documents relevant to the query (ground truth)
        arg4 : int
            The k value

        Returns
        -------
        float
            The recall value as a number between 0 and 1
        """

        recall = len(set(query_doc_IDs_ordered[:k]) & set(true_doc_IDs))/len(set(true_doc_IDs))

        #Fill in code here

        return recall


    def meanRecall(self, doc_IDs_ordered, query_ids, qrels, k):
        """
        Computation of recall of the Information Retrieval System
        at a given value of k, averaged over all the queries

        Parameters
        ----------
        arg1 : list
            A list of lists of integers where the ith sub-list is a list of IDs
            of documents in their predicted order of relevance to the ith query
        arg2 : list
            A list of IDs of the queries for which the documents are ordered
        arg3 : list
            A list of dictionaries containing document-relevance
            judgements - Refer cran_qrels.json for the structure of each
            dictionary
        arg4 : int
            The k value

        Returns
        -------
        float
            The mean recall value as a number between 0 and 1
        """

        meanRecall = 0

        for i in range(len(query_ids)):
            true_doc_IDs = [int(dic["id"]) for dic in qrels if dic["query_num"] == str(query_ids[i])]
            meanRecall += self.queryRecall(doc_IDs_ordered[i], query_ids[i],true_doc_IDs, k)

        meanRecall /= len(query_ids)

        #Fill in code here

        return meanRecall


    def queryFscore(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
        """
        Computation of fscore of the Information Retrieval System
        at a given value of k for a single query

        Parameters
        ----------
        arg1 : list
            A list of integers denoting the IDs of documents in
            their predicted order of relevance to a query
        arg2 : int
            The ID of the query in question
        arg3 : list
            The list of IDs of documents relevant to the query (ground truth)
        arg4 : int
            The k value

        Returns
        -------
        float
            The fscore value as a number between 0 and 1
        """
        
        P = self.queryPrecision(query_doc_IDs_ordered, query_id, true_doc_IDs, k)
        R = self.queryRecall(query_doc_IDs_ordered, query_id, true_doc_IDs, k)
        
        if R == 0 or P == 0:
            return 0
        fscore = (2*P*R)/(P + R)

        #Fill in code here
        

        return fscore


    def meanFscore(self, doc_IDs_ordered, query_ids, qrels, k):
        """
        Computation of fscore of the Information Retrieval System
        at a given value of k, averaged over all the queries

        Parameters
        ----------
        arg1 : list
            A list of lists of integers where the ith sub-list is a list of IDs
            of documents in their predicted order of relevance to the ith query
        arg2 : list
            A list of IDs of the queries for which the documents are ordered
        arg3 : list
            A list of dictionaries containing document-relevance
            judgements - Refer cran_qrels.json for the structure of each
            dictionary
        arg4 : int
            The k value

        Returns
        -------
        float
            The mean fscore value as a number between 0 and 1
        """

        meanFscore = 0

        for i in range(len(query_ids)):
            true_doc_IDs = [int(dic["id"]) for dic in qrels if dic["query_num"] == str(query_ids[i])]
            meanFscore += self.queryFscore(doc_IDs_ordered[i], query_ids[i],true_doc_IDs, k)

        #Fill in code here
        meanFscore /= len(query_ids)
        return meanFscore


    def queryNDCG(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
        """
        Computation of nDCG of the Information Retrieval System
        at given value of k for a single query

        Parameters
        ----------
        arg1 : list
            A list of integers denoting the IDs of documents in
            their predicted order of relevance to a query
        arg2 : int
            The ID of the query in question
        arg3 : list
            The list of IDs of documents relevant to the query (ground truth)
        arg4 : int
            The k value

        Returns
        -------
        float
            The nDCG value as a number between 0 and 1
        """
        
#         nDCG = 0
#         relevance = []
#         self.qrels = qrels
        
#         dic = [d for d in self.qrels if d["query_num"] == str(query_id)]

#         for doc in query_doc_IDs_ordered:
#             if doc in true_doc_IDs:
#                 relevance.append(dic[true_doc_IDs.index(doc)]["position"])
#             else: relevance.append(0)

#         # Discounted Cumulative Gain
#         DCG = sum([relevance[i]/log(i+1,2) for i in range(len(relevance))])

#         # Ideal relevance ordering
#         ideal_relevance = sorted(relevance,reverse = True)
#         # Ideal Discounted Cumulative Gain
#         iDCG = sum([ideal_relevance[i]/log(i+1,2) for i in range(len(relevance))])
        
#         if iDCG == 0:
#             return 0
        
#         nDCG = DCG/iDCG

#         return nDCG
         # Fill in code here
        relevance = {}
        DCG = 0
        # Since only 4 positions, starting from 4 for first position and decreasing for
        # each position, the one at position at 4 is given a relevance of 1
        MAXIMUM_RELEVANCE = 5

        DCG = 0
        iDCG = 0
        ground_truth = self.ground_truth
        if ground_truth == None:
                raise "Ground truth relevance scores not populated"
        ground_truth_ids = ground_truth.keys()
        for i, docID in enumerate(query_doc_IDs_ordered[:k]):
                if docID in ground_truth_ids:
                        DCG += (MAXIMUM_RELEVANCE - ground_truth[docID]) / log2(i + 2)
        
        sorted_ground_truths = sorted(ground_truth, key=ground_truth.get)[:k]
        for i, docID in enumerate(sorted_ground_truths):
                iDCG += (MAXIMUM_RELEVANCE - ground_truth[docID]) / log2(i + 2)
        nDCG = DCG / iDCG
        return nDCG


    def meanNDCG(self, doc_IDs_ordered, query_ids, qrels, k):
        """
        Computation of nDCG of the Information Retrieval System
        at a given value of k, averaged over all the queries

        Parameters
        ----------
        arg1 : list
            A list of lists of integers where the ith sub-list is a list of IDs
            of documents in their predicted order of relevance to the ith query
        arg2 : list
            A list of IDs of the queries for which the documents are ordered
        arg3 : list
            A list of dictionaries containing document-relevance
            judgements - Refer cran_qrels.json for the structure of each
            dictionary
        arg4 : int
            The k value

        Returns
        -------
        float
            The mean nDCG value as a number between 0 and 1
        """

#         meanNDCG = 0
#         for i in range(len(query_ids)):
#             true_doc_IDs = [int(dic["id"]) for dic in qrels if dic["query_num"] == str(query_ids[i])]
#             meanNDCG += self.queryNDCG(doc_IDs_ordered[i], query_ids[i], true_doc_IDs,k)

#         meanNDCG /= len(query_ids)
#         #Fill in code here

#         return meanNDCG
        meanNDCG = -1

        # Fill in code here
        NDCGs = []

        for query_id, query_doc_IDs_ordered in zip(query_ids, doc_IDs_ordered):
                self.ground_truth = dict((int(rel["id"]), int(rel["position"])) for rel in qrels if int(rel["query_num"]) == int(query_id))
                NDCGs.append(
                        self.queryNDCG(
                                query_doc_IDs_ordered,
                                query_id,
                                self.ground_truth.keys(),
                                k
                        )
                )

        if len(NDCGs) > 0:
                meanNDCG = sum(NDCGs) / len(NDCGs)
        return meanNDCG


    def queryAveragePrecision(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
        """
        Computation of average precision of the Information Retrieval System
        at a given value of k for a single query (the average of precision@i
        values for i such that the ith document is truly relevant)

        Parameters
        ----------
        arg1 : list
            A list of integers denoting the IDs of documents in
            their predicted order of relevance to a query
        arg2 : int
            The ID of the query in question
        arg3 : list
            The list of documents relevant to the query (ground truth)
        arg4 : int
            The k value

        Returns
        -------
        float
            The average precision value as a number between 0 and 1
        """
        avgPrecision = 0
        
        for i in range(k):
            if query_doc_IDs_ordered[i] in true_doc_IDs:
                avgPrecision += self.queryPrecision(query_doc_IDs_ordered,query_id,true_doc_IDs, i+1)
                
        rel_docs = len(true_doc_IDs)
        
        if rel_docs == 0:
            return 0
        
        avgPrecision /= rel_docs   
        
        return avgPrecision


    def meanAveragePrecision(self, doc_IDs_ordered, query_ids, q_rels, k):
        """
        Computation of MAP of the Information Retrieval System
        at given value of k, averaged over all the queries

        Parameters
        ----------
        arg1 : list
            A list of lists of integers where the ith sub-list is a list of IDs
            of documents in their predicted order of relevance to the ith query
        arg2 : list
            A list of IDs of the queries
        arg3 : list
            A list of dictionaries containing document-relevance
            judgements - Refer cran_qrels.json for the structure of each
            dictionary
        arg4 : int
            The k value

        Returns
        -------
        float
            The MAP value as a number between 0 and 1
        """

        meanAveragePrecision = 0

        for i in range(len(query_ids)):
            true_doc_IDs = [int(dic["id"]) for dic in q_rels if dic["query_num"] == str(query_ids[i])]
            meanAveragePrecision += self.queryAveragePrecision(doc_IDs_ordered[i], query_ids[i], true_doc_IDs,k)

        meanAveragePrecision /= len(query_ids)

        #Fill in code here

        return meanAveragePrecision

