class Solution(object):
    # TOPICS: ARRAY/BACKTRACKING/MATRIX
    # Search for the first character of word in the board. For all of those found positions, do a depth-first-search for the rest of the word. For each
    # recursion, clean the character in the board if it matches to avoid passing the same character multiple times. Because of Python's rules on 
    # variables and its references, after doing the search put the original character in the same position again to not impact the following searches.
    def tryWord(self, board, i, j, word):
        if len(word) == 1: return (board[i][j] == word[0])
        if (board[i][j] != word[0]): return False

        aux = board[i][j]
        board[i][j] = ""
        e, n, w, s = False, False, False, False

        if i > 0: w = self.tryWord(board, i-1, j, word[1:])
        if j > 0: n = self.tryWord(board, i, j-1, word[1:])
        if i < len(board)-1: e = self.tryWord(board, i+1, j, word[1:])
        if j < len(board[i])-1: s = self.tryWord(board, i, j+1, word[1:])
        board[i][j] = aux
        return e or n or w or s

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        k = 0
        for i in range(len(board)):
            for j in range(len(board[i])):
                if word[k] == board[i][j]:
                    t = self.tryWord(board, i, j, word)
                    if t: return True
        return False