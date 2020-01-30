# Module with classes to perform operations with strings
## import required libraries

## class definition
class indexing():
    """For efficient search in large genomes. Seed and extend."""
    def kmer(self, string):
        """Performs k-mer indexing of string"""
    def suffixTree(self, string):
        """Performs Suffix Tree indexing of string"""
    def suffixArray(self, string):
        """Performs Suffix Tree indexing of string"""
    def BurrowsWheelerTransform(self, string):
        """Performs Burrows Wheeler Transform to index a string"""
    def FullTextMinuteSpace(self, string)
        """Performs FM indexing of a string"""

class alignment():
    """Dynamic programming algorithms for string alignment"""
    def local(self, stringA, stringB, *costargs):
    def globalNeedlemanWunsch(self, stringA, stringB, *costargs):
        """Complexity: O(mn)"""
    def globalHirschberg(self, stringA, stringB, *costargs):        
        """Complexity: O(min{n,m})"""
    def computeCost(self, elA, elB, match=0, mismatch=1, gap=1):
        """Compute cost between two elements of a sequence"""
    def findOptimalPaths(self, matrix):