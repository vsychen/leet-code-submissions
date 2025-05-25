class Solution(object):
    # TOPICS: ARRAY/MATH/MATRIX
    # Base case is a matrix of length 1; in this case, return the same matrix. Starting with a matrix of length 2, it is necessary to shift the elements of the matrix so that (0,0)
    # goes to (0,1), (0,1) goes to (1,1), (1,1) goes to (1,0) and (1,0) goes to (0,0). Using one extra variable to hold the element being shifted, run counter-clockwise so that the
    # data that was in some position is already saved in another position. [aux <- (0,0); (0,0) <- (1,0); (1,0) <- (1,1); (1,1) <- (0,1); (0,1) <- aux]
    # When drew, the matrix NxN has the shape of a square and, for this reason, should need only four changes for each iteration, no matter the length of its side.
    # For matrix of length greater than 3, after shifting the outer elements, it is necessary to shift the inner elements. Because of question constraints, it is not possible to 
    # use recursion and create a copy of the inner matrix, so it is necessary to add another loop, to keep watch of those inner iterations. N=2 and N=3 should have only 1 iteration;
    # N=4 and N=5 should have 2 iterations; N=6 and N=7 should have 3 iterations an so on. Note that both i and j should have different start and end values for each of these inner 
    # iterations. On the outer iteration, i and j both start with 0 and end in len(matrix)-1; On the first inner iteration, i and j start with 1 and end in len(matrix)-2, and so on.
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        l1 = len(matrix)
        if l1 <= 1: return

        for i in range(l1>>1):
            l2 = l1 - (i<<1)
            for j in range(i, i+l2-1):
                aux = matrix[i][j]
                matrix[i][j] = matrix[l1-1-j][i]
                matrix[l1-1-j][i] = matrix[l1-1-i][l1-1-j]
                matrix[l1-1-i][l1-1-j] = matrix[j][l1-1-i]
                matrix[j][l1-1-i] = aux