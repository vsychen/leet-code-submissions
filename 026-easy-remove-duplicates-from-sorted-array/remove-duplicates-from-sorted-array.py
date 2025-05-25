class Solution(object):
    # TOPICS: ARRAY
    # The list is sorted, so check if the element has the same value as the next element. If yes, remove the next element (do not go to the next element yet, because
    # it is possible to have more than duplicates). If not duplicate, go to the next element.
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1: return 1
        i = 0
        while i < len(nums)-1:
            if nums[i] == nums[i+1]:
                nums.pop(i+1)
            else:
                i += 1
        return len(nums)