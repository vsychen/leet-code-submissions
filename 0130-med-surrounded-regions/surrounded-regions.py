class Solution(object):
    # TOPICS: MATRIX/BFS
    # If any dimension of the board is of length 2 or less, return the board as it is, because any "O" will be on the edge of the board. For boards of size 3 or
    # more, check the edges for "O"s For any "O" found, change it to another character, "1" for example. Then, propagate these changes to any adjacent "O"s
    # (up, down, left, right). After changing any edge's "O"s and its adjacent "O"s, change any remaining "O"s to "X". And then change any "1" back to "O".
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if len(board) <= 2 or len(board[0]) <= 2: return board

        def propagate(i, j):
            board[i][j] = "1"

            if i-1 >= 0 and board[i-1][j] == "O": propagate(i-1, j)
            if i+1 < len(board) and board[i+1][j] == "O": propagate(i+1, j)
            if j-1 >= 0 and board[i][j-1] == "O": propagate(i, j-1)
            if j+1 < len(board[i]) and board[i][j+1] == "O": propagate(i, j+1)

        for j in range(len(board[0])):
            if board[0][j] == "O": propagate(0, j)
            if board[len(board)-1][j] == "O": propagate(len(board)-1, j)

        for i in range(len(board)):
            if board[i][0] == "O": propagate(i, 0)
            if board[i][len(board[i])-1] == "O": propagate(i, len(board[i])-1)
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "1":
                    board[i][j] = "O"