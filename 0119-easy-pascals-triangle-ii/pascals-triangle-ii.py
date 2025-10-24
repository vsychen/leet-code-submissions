class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        
        pascal = {0:[1], 1:[1,1]}

        if rowIndex in pascal: return pascal[rowIndex]
        else:
            aux = self.getRow(rowIndex-1)
            new_row = [1] + [aux[i]+aux[i+1] for i in range(len(aux)-1)] + [1]
            pascal[rowIndex] = new_row
            return pascal[rowIndex]