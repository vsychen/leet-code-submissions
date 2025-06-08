class Solution(object):
    # TOPICS: ARRAY/MATRIX
    # First, check if elements from a row are duplicated (except ".", which can be duplicated). Then, transpose the matrix and check if the elements of the columns (now, rows) 
    # are duplicated. At last, split the lists in groups of three numbers and organize them in three groups of three numbers (each of them being one small square) and then 
    # check if there are duplicated elements in them.
    def isValid(self, l):
        return len(l) == len(set(l))

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            if not self.isValid([a for a in board[i] if a != "."]):
                return False

        board2 = [[board[j][i] for j in range(9)] for i in range(9)]
        for i in range(9):
            if not self.isValid([a for a in board2[i] if a != "."]):
                return False
        
        temp = [board[i][j:j+3] for j in range(0, 9, 3) for i in range(9)]
        board3 = [[b for bs in temp for b in bs][i:i+9] for i in range(0, 81, 9)]
        for i in range(9):
            if not self.isValid([a for a in board3[i] if a != "."]):
                return False
        
        return True