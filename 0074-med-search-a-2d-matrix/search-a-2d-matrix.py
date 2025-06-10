class Solution(object):
    # TOPICS: ARRAY/MATRIX
    # Search the first element of each row, while it's less than the target value. If it's the target value, return True; if all rows' first element are
    # less than the target value, check the last row, element by element; otherwise, return one row (last row that the first element is less than the
    # target value) and check this row's elements one-by-one. If the target value is found, return True; otherwise, return False.
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        i,j = 0,0
        if matrix[i][j] == target: return True
        while i < len(matrix)-1 and matrix[i][0] < target: 
            i += 1
            if matrix[i][j] == target: return True
        if matrix[i][j] > target: i -= 1
        while j < len(matrix[i])-1 and matrix[i][j] < target: j += 1
        return matrix[i][j] == target
    
a = Solution()
print(a.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 30))