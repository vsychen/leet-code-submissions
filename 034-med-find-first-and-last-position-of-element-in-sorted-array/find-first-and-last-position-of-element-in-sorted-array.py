class Solution(object):
    # ALGORITHM: DIVIDE AND CONQUER/BINARY SEARCH
    # First, do the classic binary search. If target not found, return -1. If target found, search for the first and last occurrence of target. Because the list is sorted, all
    # occurrences of target are at grouped together.
    def binarySearch(self, nums, target):
        if len(nums) == 0: return -1
        elif len(nums) == 1: return 0 if nums[0] == target else -1

        mid = len(nums)>>1

        if nums[mid] == target: return mid
        elif nums[mid] > target: 
            temp = self.binarySearch(nums[:mid], target)
            return temp if temp != -1 else -1
        elif nums[mid] < target: 
            temp = self.binarySearch(nums[mid+1:], target)
            return mid+1+temp if temp != -1 else -1

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ind = self.binarySearch(nums, target)
        i = j = ind
        if ind != -1:
            while i > 0:
                i -= 1
                if nums[i] != target:
                    i += 1
                    break
            
            while j < len(nums)-1:
                j += 1
                if nums[j] != target:
                    j -= 1
                    break
        
        return [i, j]