class Solution(object):
    # ALGORITHM: NONE
    # Starting from the end, search for first occurrence of nums[i-1] < nums[i]. Save nums[i-1] and, starting from the end again, search for first occurrence of 
    # nums[i-1] < nums[j]. Switch those two numbers and sort the elements of nums from i onwards, while maintaining the order for the previous elements.
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