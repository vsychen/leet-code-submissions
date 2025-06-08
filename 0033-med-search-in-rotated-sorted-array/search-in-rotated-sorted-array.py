class Solution(object):
    # TOPICS: ARRAY/BINARY SEARCH
    # First, to find how much the sorted list is dislocated, a modified binary search is used. Instead of finding the target number, it searches for the lesser value using binary search.
    # With the position of the lesser value found, the list can be rearranged to be sorted again and, this time, a classic binary search is used to find the value. At the end, it is
    # necessary to sum the index of the target with the list offset and return the module of this sum, which will be the index of the element in the dislocated list.
    # Observation: if the element is not on the list, return -1.
    def findPivot(self, nums):
        if len(nums) == 0: return (-1, -1)
        elif len(nums) == 1: return (0, nums[0])
        elif len(nums) == 2: return (0, nums[0]) if nums[0] < nums[1] else (1, nums[1])

        mid = len(nums)>>1
        a1 = False
        a2 = False

        if mid == 1 or nums[0] < nums[mid-1]:
            a1 = True
        if nums[mid] < nums[-1]:
            a2 = True

        if a1 and a2:
            return (0, nums[0]) if nums[0] < nums[mid] else (mid, nums[mid])
        elif a2:
            return self.findPivot(nums[:mid])
        else:
            (ind, val) = self.findPivot(nums[mid:])
            return (ind+mid, val)

    def binarySearch(self, nums, target):
        if len(nums) == 0: return -1
        elif len(nums) == 1: return 0 if nums[0] == target else -1
        mid = len(nums)>>1

        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            ind = self.binarySearch(nums[:mid], target)
            return ind if ind != -1 else -1
        elif nums[mid] < target:
            ind = self.binarySearch(nums[mid+1:], target)
            return (mid+1+ind) if ind != -1 else -1

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        (ind, val) = self.findPivot(nums)
        nums = nums[ind:]+nums[:ind]
        bs = self.binarySearch(nums, target)

        return (ind+bs)%len(nums) if bs != -1 else -1

    # Oh yeah, for some reason, this works too
    # def search(self, nums, target):
    #     """
    #     :type nums: List[int]
    #     :type target: int
    #     :rtype: int
    #     """
    #     try:
    #         return nums.index(target)
    #     except:
    #         return -1