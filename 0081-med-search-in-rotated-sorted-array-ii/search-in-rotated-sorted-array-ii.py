class Solution(object):
    # TOPICS: ARRAY/BINARY SEARCH
    # Get the start and end values; if any of them are the target, return True. If the target is lower than the first value and higher than the end value
    # (this could happen if the list got shifted) or if the length of the list is less or equal than 2 (this would mean the value is not in this list, as 
    # the start and end values were already checked), return False.
    # Get the mid value of the list. If the mid value is the target, return True. If the start, mid and end values are the same, the target value could be
    # anywhere in the technically unsorted list, so just check if its present (built-in ~in~ operator). If start and mid values are equal, check if the target
    # value is at the end sublist. If mid and end values are equal, check if the target value is at the start sublist. If start and end are equal, remove both
    # ends and check if the value is at the sublist.
    # For the remaining cases, if start is less than mid and target is less than mid, it could be anywhere, check both sublists (start and end), otherwise, it
    # can only be at the end sublist; if mid is less than end and target is less than mid, it could only be at the start sublist, otherwise
    # it can be on both sublists (start and end). Continue searching for the value recursively until the base case is reached.
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums: return False
        start = nums[0]
        end = nums[-1]

        if target == start or target == end: return True
        elif (target < start and target > end) or (len(nums) <= 2): return False

        mid = len(nums) >> 1

        if nums[mid] == target: return True

        if start == nums[mid] and start == end: 
            return target in nums
        elif start == nums[mid]:
            return self.search(nums[mid+1:-1], target)
        elif nums[mid] == end:
            return self.search(nums[1:mid], target)
        elif start == end:
            return self.search(nums[1:-1], target)
        elif start < nums[mid]:
            if target < nums[mid]: return self.search(nums[1:mid], target) or self.search(nums[mid+1:-1], target)
            else: return self.search(nums[mid+1:-1], target)
        elif nums[mid] < end:
            if target < nums[mid]: return self.search(nums[1:mid], target)
            else: return self.search(nums[1:mid], target) or self.search(nums[mid+1:-1], target)