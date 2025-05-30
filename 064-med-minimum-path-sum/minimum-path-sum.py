class Solution(object):
    # TOPICS: MATRIX
    # Start by updating the values of the elements in the first row and first column to the sum of the value at (i,j) and (i-1,j)/(i,j-1). Then, for each (i,j) starting from (1,1), 
    # update its value to the minimum value between the sum of (i,j) and (i-1,j)/(i,j-1). At the end, return the value at the last position of the matrix.
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        for i in range(1, len(grid)):
            grid[i][0] = grid[i-1][0] + grid[i][0]
        for j in range(1, len(grid[0])):
            grid[0][j] = grid[0][j-1] + grid[0][j]

        for j in range(1, len(grid)):
            for i in range(1, len(grid[j])):
                grid[j][i] = min(grid[j][i-1]+grid[j][i], grid[j-1][i]+grid[j][i])
        return grid[-1][-1]