class Solution(object):
    # TOPICS: STRING
    # Calculate the total num of columns and rows that the matrix will have. Fill the matrix with the string characters using the pattern mentioned.
    # Transpose the matrix, so that the rows become the columns and the columns become the rows.
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1: return s
        numReps = int(len(s)/((numRows<<1)-2))
        numCols = numReps*(numRows-1)
        result = []
        ls = list(s)

        for _ in range(numReps+1):
            for x in range(numRows-1):
                temp = []
                if x == 0:
                    for j in range(numRows):
                        if len(ls) == 0: temp.append("")
                        else: temp.append(ls.pop(0))
                else:
                    for j in range(numRows):
                        if len(ls) == 0: temp.append("")
                        elif j == numRows-x-1: temp.append(ls.pop(0))
                        else: temp.append("")
                result.append(temp)
                if len(ls) == 0: break

        final = [[result[j][i] for j in range(len(result))] for i in range(len(result[0]))]
        return "".join("".join(x) for x in final)
