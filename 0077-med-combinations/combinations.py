class Solution(object):
    # TOPICS: BACKTRACKING
    # If k = 1, return a list of lists, where each element is a list of one element from 1 to n. If k > 1, find the combinations for k-1 and combine with
    # each element of the list [1...n].
    def doTheTrick(self, lst, k):
        if k == 1: return [[x] for x in lst]
        else: 
            r = []
            for i in range(len(lst)):
                r.extend([lst[i]]+x for x in self.doTheTrick(lst[i+1:], k-1))
            return r

    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        return self.doTheTrick([x for x in range(1, n+1)], k)