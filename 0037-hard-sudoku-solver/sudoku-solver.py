class Solution(object):
    # TOPICS: MATRIX/BACKTRACKING
    # Test all possible combinations until the correct combination is found. For each position (i,j) check the same row, same column and same square
    # for the numbers already placed; make the choices list the numbers not found in them. For each possible choice, check the next '.' character and
    # its possibilities. If the matrix goes all the way to the end (i=9,j=9), the valid answer has been found; If a null matrix has returned, the
    # combination is invalid, try other combination.
    # Obs: This answer is not accepted by LeetCode (python3), it goes TLE on testcase 6/7. However, using the same logic but in another programming 
    # language (Java) succeeds.
    def getRow(self, board, i):
        return board[i]

    def getColumn(self, board, j):
        return [board[i][j] for i in range(9)]

    def getSquare(self, board, i, j):
        temp = [board[i][j:j+3] for j in range(0,9,3) for i in range(9)]
        i = i//3
        j = j//3

        k = i*3 + j*9
        return [x for t in temp[k:k+3] for x in t]

    def getChoices(self, row, column, square):
        return [x for x in ["1","2","3","4","5","6","7","8","9"] if x not in row and x not in column and x not in square]
    
    def nextMove(self, board, i, j):
        nextI = i+1 if j == 8 else i
        nextJ = 0 if j == 8 else j+1

        if i >= 9 or j >= 9: return board
        if board[i][j] != ".":
            return self.nextMove(board, nextI, nextJ)
        else:
            row = [x for x in self.getRow(board, i) if x != "."]
            column = [x for x in self.getColumn(board, j) if x != "."]
            square = [x for x in self.getSquare(board, i, j) if x != "."]
            choices = self.getChoices(row, column, square)
            if not choices: return []

            aux = []
            for c in choices:
                board[i][j] = c
                aux = self.nextMove(board, nextI, nextJ)
                if not aux: board[i][j] = '.'
                else: break

            return aux

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        return self.nextMove(board, 0, 0)

a = Solution()
print(a.solveSudoku([["5","3",".",".","7",".",".",".","."],
                   ["6",".",".","1","9","5",".",".","."],
                   [".","9","8",".",".",".",".","6","."],
                   ["8",".",".",".","6",".",".",".","3"],
                   ["4",".",".","8",".","3",".",".","1"],
                   ["7",".",".",".","2",".",".",".","6"],
                   [".","6",".",".",".",".","2","8","."],
                   [".",".",".","4","1","9",".",".","5"],
                   [".",".",".",".","8",".",".","7","9"]], 
                  ))