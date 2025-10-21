class Solution(object):
    # TOPICS: STRING/DYNAMIC PROGRAMMING
    # If the elements in s1+s2 are different from s3, s3 is not an interleave of s1 and s2. if s1+s2 or s2+s1 are equal to s3, s3 is an interleave of s1 and s2.
    # Create a table where each entry dp[i][j] indicates whether the substring of s3 up to position i+j can be formed by interleaving the substrings of s1 up to i and s2 up to j. 
    # Initialize the base for empty strings and iteratively fill the table, checking if each character of s3 can be reached by adding a character from s1 or s2.
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if sorted(s1+s2) != sorted(s3): return False
        elif s1+s2 == s3 or s2+s1 == s3: return True

        def procceed(s1, s2, s3, b=False):
            matrix = [[False for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
            matrix[0][0] = True

            for i in range(len(s1)):
                if s1[i] == s3[i]:
                    matrix[i+1][0] = True
            
            for i in range(len(s2)):
                if s2[i] == s3[i]:
                    matrix[0][i+1] = True

            for i in range(len(s1)):
                for j in range(len(s2)):
                    k = i+j+1
                    matrix[i+1][j+1] = (matrix[i][j+1] and s1[i] == s3[k]) or (matrix[i+1][j] and s2[j] == s3[k])

            return matrix[-1][-1]
        
        return procceed(s1, s2, s3, False)