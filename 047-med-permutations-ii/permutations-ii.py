class Solution(object):
    # TOPICS: ARRAY
    # Using recursion, the base case is when the list has length of 1. For each recursion, concatenate each character with the list from next level recursion excluding the character
    # to be concatenated. If said permutation is not on the answer yet, add it to the answer list. If it is, skip it and go check the next.
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 1: return [nums]
        r = []
        for i in range(len(nums)):
            permutations = self.permuteUnique(nums[:i]+nums[i+1:])
            a = [[nums[i]]+p for p in permutations]
            for j in range(len(a)):
                if a[j] not in r: r.append(a[j])
        return r