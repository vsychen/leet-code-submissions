class Solution(object):
    def sortedInReverse(self, nums):
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]: return False
        return True

    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1: pass
        elif self.sortedInReverse(nums): 
            nums.reverse()
        else:
            i = len(nums)-1
            while i > 0 and nums[i] <= nums[i-1]:
                i -= 1
            
            curr = nums[i-1]

            j = len(nums)-1
            while j > i and nums[j] <= curr:
                j -= 1

            nums[i-1] = nums[j]
            nums[j] = curr
            nums[i:] = sorted(nums[i:])