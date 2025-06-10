class Solution(object):
    # TOPICS: BACKTRACKING
    # Base case, nums = []; return [[]]. Append nums to the answer and then, for each element of the list nums, call the same method without that element.
    # When appending the lists to the answer, do not append if they are already in the subset.
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums == []: return [[]]
        r = []
        r.append(nums)
        for i in range(len(nums)):
            aux = self.subsets(nums[:i]+nums[i+1:])
            for x in aux:
                if x not in r: r.append(x)
        return r