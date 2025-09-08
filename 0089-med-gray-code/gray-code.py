class Solution(object):
    # TOPICS: BACKTRACKING/BIT MANIPULATION
    # The base case, n = 1, the elements are '0' and '1'. For any n > 1, generate the elements of n-1. Append '0' to these elements to create the first half of the new list.
    # Append '1' to these elements in a reverse order to create the second half of the new list. Concatenate the two lists. Remember to cast the elements to integer when finished.
    def generateElements(self, n):
        if n == 1: return ['0', '1']
        else:
            sublist = self.generateElements(n-1)
            first = ['0'+x for x in sublist]
            second = ['1'+x for x in reversed(sublist)]
            return first+second
        
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n < 1: return []
        elif n == 1: return [0, 1]

        return [int(x, 2) for x in self.generateElements(n)]