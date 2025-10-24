class Solution(object):
    # TOPICS: ARRAY/DYNAMIC PROGRAMMING
    # If the triangle has only one line, it has only one element, return its value as the answer. For the rest of the cases, check each row and update its value with the sum
    # of the current value (triangle[x][y]) and the minimum value between the values above (triangle[x-1][y-1] and triangle[x-1][y]). At the end of the iteration, the last row
    # will have the sums to reach each of the positions. Search for the lesser value and it will be the answer.
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if len(triangle) == 1: return triangle[0][0]

        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i-1][j-1] if j > 0 else 10000, triangle[i-1][j] if j < len(triangle[i])-1 else 10000)
        
        return min(triangle[-1])