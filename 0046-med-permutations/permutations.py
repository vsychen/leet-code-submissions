class Solution(object):
    # TOPICS: ARRAY
    # Using recursion, the base case is when the list has length of 1. For each recursion, concatenate each character with the list from next level recursion excluding the character
    # to be concatenated. Then group all the permutations together and return.
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 1: return [nums]
        r = []
        for i in range(len(nums)):
            permutations = self.permute(nums[:i]+nums[i+1:])
            a = [[nums[i]]+p for p in permutations]
            r.extend(a)
        return r