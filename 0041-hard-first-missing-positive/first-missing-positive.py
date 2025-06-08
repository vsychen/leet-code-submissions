class Solution(object):
    # TOPICS: ARRAY
    # The maximum value the missing positive can be is the length of the list (if a list of length 5 has all numbers in the range, it should have 1,2,3,4,5 on the list, not necessarily
    # in this order, but the maximum value will be the length of the list). In the eventual case that not all numbers in the range are present on the list (if one of the numbers is 
    # duplicated, or outside the value range), there will be a vacancy in the range.
    # To find this vacancy, first change all outside range values to a value exceeding the length of the list (ex.: l+1). For each number on the list, search for the corresponding
    # position in the list and flip its value (turn negative). The signal will be only to mark if the element is on the list. Continue getting the absolute value as index and flipping
    # the signal for each number in the list range. When finished, check for the first value that is positive (was not found in the numbers list). If all numbers were found, then the
    # first missing positive is the length of the list plus one (l+1).
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        for i in range(l):
            if nums[i] <= 0 or nums[i] > l: nums[i] = l+1
        
        for i in range(l):
            aux = nums[i] if nums[i] > 0 else -nums[i]
            if aux <= l:
                if nums[aux-1] > 0:
                    nums[aux-1] = -nums[aux-1]
        
        for i in range(l):
            if nums[i] > 0:
                return i+1
        
        return l+1

a = Solution()
print(a.firstMissingPositive([3,4,-1,1]))