class Solution(object):
    # TOPICS: ARRAY/BINARY SEARCH
    # Classic binary search. If found, return index. If not found, return index of the first element greater than target instead of -1.
    def binarySearch(self, nums, target):
        if len(nums) == 0: return 0
        elif len(nums) == 1: return 0 if nums[0] >= target else 1

        mid = len(nums)>>1

        if nums[mid] == target: return mid
        elif nums[mid] > target: 
            return self.binarySearch(nums[:mid], target)
        elif nums[mid] < target: 
            return mid+1+self.binarySearch(nums[mid+1:], target)

    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.binarySearch(nums, target)