class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        for i in range(0, len(nums)-1, 1):
            for j in range(i+1, len(nums), 1):
                if nums[i] + nums[j] == target:
                    result = [i, j]
        return result