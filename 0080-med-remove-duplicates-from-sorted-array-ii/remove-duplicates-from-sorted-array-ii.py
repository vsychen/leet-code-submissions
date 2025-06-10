class Solution(object):
    # TOPICS: ARRAY
    # Create two variables, curr is the current character and count is the count of said character in the list nums. Traverse the list increasing the 
    # counter and, when nums[i] is different than curr, update curr and set the counter to zero. When the counter is greater than 2, remove the element
    # at that position. Increase the index only when not removing an element, to avoid skipping duplicates.
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr = "."
        count = 0
        index = 0
        while index < len(nums):
            if curr != nums[index]:
                curr = nums[index]
                count = 0
            
            count += 1
            if count >= 3:
                nums.pop(index)
            else:
                index += 1