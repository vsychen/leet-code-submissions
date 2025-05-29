class Solution(object):
    # TOPICS: MATRIX
    # Base cases are, if n==1, return a matrix of one element; if n==2, return a 2x2 matrix where the third and fourth numbers are switched up. To fill up the matrix, fill only the outer
    # layer and repeat the steps for the inner matrix. Per the question constraints, the elements of the matrix will be an increment. The upper part of the matrix will have the first n
    # elements plus the offset (in case of a recursion). The right-side of the matrix will have the i elements after the first n elements (1 < i < n) plus offset. The bottom part of the 
    # matrix are between 2n and 3n-2. The left-side of the matrix will have the numbers between 3n-1 to 4n-4. The offset of a iteration is the same value as the 4n-4 value of the previous
    # iteration (after filling the outer layer, the inner matrix will be filled too, starting with the value at the last position from the outer layer).
    def doTheTrick(self, n, offset=0):
        if n == 1: return [[1+offset]]
        elif n == 2: return [[1+offset,2+offset], [4+offset,3+offset]]
        r = [[0]*n for _ in range(n)]
        
        r[0] = [i+1+offset for i in range(n)]
        r[-1] = [i+offset for i in range((3*n)-2,(2*n)-2,-1)]

        for i in range(1, n-1):
            r[i][0] = (n<<2)-3-i+offset
            r[i][-1] = n+i+offset

        aux = self.doTheTrick(n-2,r[1][0])
        
        for i in range(1, n-1):
            r[i][1:-1] = aux[i-1]

        return r

    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        return self.doTheTrick(n, 0)