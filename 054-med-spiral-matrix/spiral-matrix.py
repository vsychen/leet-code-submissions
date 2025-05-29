class Solution(object):
    # TOPICS: ARRAY/MATRIX
    # To get the spiral order of a matrix, first get the first row of a matrix. Then, get the last elements from each row still remaining. Then get the last row, but in a reverse order.
    # Then, get the first elements of the remaining rows, in a reverse order. Finally, redo all these four steps until the original matrix is empty.
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        lm = len(matrix)
        if lm == 0: return []
        elif lm == 1: return matrix[0]

        r = matrix.pop(0)
        if not matrix: return r

        for i in range(len(matrix)):
            r.append(matrix[i].pop())
        matrix = [m for m in matrix if m != []]
        if not matrix: return r
        
        r.extend(matrix.pop()[::-1])
        if not matrix: return r

        for i in range(len(matrix)-1,-1,-1):
            r.append(matrix[i].pop(0))
        matrix = [m for m in matrix if m != []]
        if not matrix: return r
        
        r.extend(self.spiralOrder(matrix))
        
        return r