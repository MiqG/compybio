# Module with classes to perform operations with strings
## import required libraries
import numpy as np

## class definition
class indexing():
    """For efficient search in large genomes. Seed and extend."""
    def generateBiostring(self, stringType, length):
        vocab = {'DNA': np.array(['A','C','T','G']),
                'RNA': np.array(['A','C','U','G'])}
        chosenVocab = vocab[stringType]
        idxRand = np.random.randint(0,len(chosenVocab), size = length)
        return ''.join(chosenVocab[idxRand])

    def getKmerIndex(self, biostring, sizeKmer):
        index = []
        for i in range(len(biostring) - sizeKmer + 1):
            index.append((biostring[i:i+sizeKmer], i))
            index.sort()
        return index

    def queryKmerIndex(self, querySeq, kmerIndex):
        "Return which kmers contain the querySeq."
        idxs = np.array(range(len(kmerIndex)))
        for i, ntQuery in enumerate(querySeq):
            for idx in idxs:
                if kmerIndex[np.asscalar(idx)][0][i] != ntQuery:
                    idxs = idxs[idxs != idx]
        hits = [kmer[1] for i, kmer in enumerate(kmerIndex) if i in idxs]
        return hits
    
    
    
#     def suffixTree(self, string):
#         """Performs Suffix Tree indexing of string"""
#     def suffixArray(self, string):
#         """Performs Suffix Tree indexing of string"""
#     def BurrowsWheelerTransform(self, string):
#         """Performs Burrows Wheeler Transform to index a string"""
#     def self.FullTextMinuteSpace(self, string)
#         """Performs FM indexing of a string"""

# class alignment():
#     """Dynamic programming algorithms for string alignment"""
#     def local(self, stringA, stringB, *costargs):
#     def globalNeedlemanWunsch(self, stringA, stringB, *costargs):
#         """Complexity: O(mn)"""
#     def globalHirschberg(self, stringA, stringB, *costargs):        
#         """Complexity: O(min{n,m})"""
#     def computeCost(self, elA, elB, match=0, mismatch=1, gap=1):
#         """Compute cost between two elements of a sequence"""
#     def findOptimalPaths(self, matrix):