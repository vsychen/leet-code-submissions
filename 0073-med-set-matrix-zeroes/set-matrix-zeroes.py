class Solution(object):
    # TOPICS: MATRIX
    # Question asked for constant space solution; to meet this requirement, changes are done only in the given matrix. First, change the type of the zeroes to
    # string. Second, for each stringfied zero, change all elements in the same row/column to zero, except for the stringfied zeroes. Finally, change the type of
    # all stringfied zeroes back to integer. The cast from integer to string is to identify which zeroes should propagate the changes to the row/column; if
    # the changes are made without knowing the starting zeroes, the final matrix would always be a zeroed matrix.
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0: matrix[i][j] = "0"

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "0":
                    for k in range(len(matrix)):
                        if matrix[k][j] != "0": matrix[k][j] = 0
                    for k in range(len(matrix[0])):
                        if matrix[i][k] != "0": matrix[i][k] = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "0": matrix[i][j] = 0