class Solution(object):
    # TOPICS: ARRAY/DYNAMIC PROGRAMMING
    # Base cases, first row is [1], second row is [1,1]. For the remaining rows, create a new_row with the sum of row[i] and row[i+1] elements. Add [1] to the start and to the end
    # of the list. Add this new row to the answer dictionary. For the answer, present just all the values corresponding to the keys less than or equal to the number of rows asked.
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        pascal = {1:[1], 2:[1,1]}

        def getRow(row):
            if row in pascal: return pascal[row]
            else:
                aux = getRow(row-1)
                new_row = [1] + [aux[i]+aux[i+1] for i in range(len(aux)-1)] + [1]
                pascal[row] = new_row
                return pascal[row]
        
        getRow(numRows)
        return [v for (k,v) in pascal.items() if k <= numRows]