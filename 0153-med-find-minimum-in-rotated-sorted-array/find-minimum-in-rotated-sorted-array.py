class Solution(object):
    # TOPICS: ARRAY/BINARY SEARCH
    # If len(nums)==1, return it as the answer. If len(nums)==2, return the smaller value as the answer. For bigger cases, pick the middle index and check
    # the value at that position i against the value at position i-1 and i+1. If the middle value is bigger than the value at i-1 and smaller than the 
    # value at i+1, return it as the answer. Otherwise, split the list into two and repeat the search with both halves, before comparing the smaller value
    # from the left against the smaller value from the right.
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1: return nums[0]
        elif len(nums) == 2: return nums[0] if nums[0] < nums[1] else nums[1]

        mid = len(nums)>>1
        if nums[mid-1] > nums[mid] and nums[mid] < nums[mid+1]: return nums[mid]
        else:
            left = self.findMin(nums[:mid+1])
            right = self.findMin(nums[mid:])
            return left if left < right else right