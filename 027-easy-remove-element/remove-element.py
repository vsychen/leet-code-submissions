class Solution(object):
    # ALGORITHM: BRUTE FORCE
    # Check elements of the list. If element = val, remove from list. Return the size of the list.
    # Observation: The question requires that the changes occurs in-place, so attributing a list comprehension to the variable nums was not a valid choice.
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        while i < len(nums):
            if nums[i] == val: nums.pop(i)
            else: i += 1
        return len(nums)