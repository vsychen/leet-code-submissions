class Solution(object):
    # TOPICS: MATRIX
    # Change the grid, instead of 1 use -1, and instead of 0 use the number of paths until that position. The first row and first column has only one path for all its positions (except 
    # if its an obstacle). Starting from position (1,1), the number of paths to a said position is equal to the number of paths to its previous positions, namely (x-1,y) and (x, y-1).
    # If one position is not an obstacle, check if the previous positions are obstacles; if they are not, add their value to the value of the current position. At the end, return the
    # value of the last position in the matrix (end point).
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1: return 0
        grid = [[-1 if obstacleGrid[i][j] == 1 else 0 for j in range(len(obstacleGrid[i]))] for i in range(len(obstacleGrid))]

        for i in range(len(grid[0])):
            if grid[0][i] == 0: grid[0][i] = 1
            else: break
        
        for i in range(1, len(grid)):
            if grid[i][0] == 0: grid[i][0] = 1
            else: break

        for i in range(1, len(grid)):
            for j in range(1, len(grid[i])):
                if grid[i][j] != -1:
                    up = grid[i][j-1]
                    if up != -1: grid[i][j] += up
                    left = grid[i-1][j]
                    if left != -1: grid[i][j] += left
        
        return grid[-1][-1]