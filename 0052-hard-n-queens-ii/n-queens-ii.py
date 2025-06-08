class Solution(object):
    # TOPICS: ARRAY/BACKTRACKING
    # The scenarios where there's n queens in a NxN board can be replaced by a equivalent combination. It works because there's only one queen in a row
    # (in the combination, the integer will refer to the position of the queen), one queen in a column (there's will be no repetition of elements). The
    # only case that need to be tested is the diagonals; the queens will be in a diagonally-invalid position if abs(x2-x1) = abs(y2-y1) where (x1,y1) 
    # is the position of the first queen and (x2,y2) is the position of the second queen.
    # First get all combinations for 1<=i<=n. Check if each combination is valid (each row will have only one queen; as there's no repetition, 
    # there will be only one queen per column too; the combination is valid diagonally if abs(x2-x1) is different to y2-y1 for each pair of queens)
    # The answer will be the number of valid combinations.
    def getCombinations(self, numbers):
        if len(numbers) == 1: return [numbers]
        r = []
        for i in range(len(numbers)):
            r.extend([[numbers[i]]+e for e in self.getCombinations(numbers[:i]+numbers[i+1:])])
        return r
    
    def isValid(self, combination):
        for i in range(len(combination)-1):
            for j in range(i+1, len(combination)):
                if abs(combination[i] - combination[j]) == j-i: return False
        return True

    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1: return 1
        elif n == 2 or n == 3: return 0

        combinations = self.getCombinations([x+1 for x in range(n)])
        validCombinations = [c for c in combinations if self.isValid(c)]
        return len(validCombinations)