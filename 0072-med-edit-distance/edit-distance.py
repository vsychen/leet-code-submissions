class Solution(object):
    # TOPICS: STRING
    # If the words are the same, there's no distance between them. If there's no common characters in the words, the minimum distance is the length of the longest
    # word. If both words have a prefix or a suffix, its also possible to remove them without changing the result. If one of the words is an empty string, 
    # the minimum distance is the length of the other word.
    # Create a matrix with dimensions length(word1) x length(word2) (obs.: it's not length(word1)-1 x length(word2)-1 because this question needs to compute
    # the empty string too). While traversing the matrix, if i or j is 0, matrix[i][j] is max(i,j) because it's necessary to insert i/j characters to go from 
    # an empty string to the word at i/j position. For each position (i,j), if word1[i-1] == word2[j-1], (i,j) = (i-1,j-1), because there's no need to change
    # anything; on the other hand, if they are different, (i,j) = 1+min((i-1,j-1), (i-1,j), (i,j-1)) where (i-1,j-1), (i-1,j) and (i,j-1) represents the 
    # replace, delete and insert actions, respectively.
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if word1 == word2: return 0
        if len([c for c in word2 if c in word1]) == 0: return max(len(word1), len(word2))

        while word1 and word2 and word1[0] == word2[0]:
            word1 = word1[1:]
            word2 = word2[1:]
        
        while word1 and word2 and word1[-1] == word2[-1]:
            word1 = word1[:-1]
            word2 = word2[:-1]

        if not word1 or not word2: return max(len(word1), len(word2))

        matrix = [[500 for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i == 0: matrix[0][j] = j
                elif j == 0: matrix[i][0] = i
                elif word1[i-1] == word2[j-1]: matrix[i][j] = matrix[i-1][j-1]
                else: matrix[i][j] = 1+min(matrix[i-1][j-1], matrix[i-1][j], matrix[i][j-1])
        return matrix[-1][-1]