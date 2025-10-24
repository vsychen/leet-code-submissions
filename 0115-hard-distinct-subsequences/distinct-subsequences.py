class Solution(object):
    # TOPICS: STRING/DYNAMIC PROGRAMMING
    # Create a matrix len(s) x len(t). At the first row, change the matrix[i][j] to 1 where s[j] == t[i]. For the subsequent rows, use a counter to know how many ways there are to
    # get to that situation, adding matrix[i-1][j] every time it is different than 0. Every time s[j] == t[i], put the counter value as the value of matrix[i][j]. When all rows are
    # filled, sum all values from the last row and that will be the answer.
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        matrix = [[0 for _ in range(len(s))] for _ in range(len(t))]

        for i in range(len(t)):
            if i == 0:
                for j in range(len(s)):
                    if s[j] == t[i]: matrix[i][j] += 1
            else:
                counter = 0
                for j in range(len(s)):
                    if s[j] == t[i]: matrix[i][j] = counter
                    if matrix[i-1][j] != 0: counter += matrix[i-1][j] 

        return sum(matrix[-1])