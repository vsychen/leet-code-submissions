class Solution(object):
    # TOPICS: ARRAY/SORTING
    # There are only three values in the list, 0, 1 and 2. To solve this problem using constant space, make three variables; one for each possible value.
    # For each element, increment the corresponding variable. After searching the whole list, replace the list's values according to the variables.
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1: return nums
        else:
            zeroes, ones, twos = 0, 0, 0
            for n in nums:
                if n == 0: zeroes += 1
                elif n == 1: ones += 1
                else: twos += 1
            
            for i in range(len(nums)):
                if zeroes > 0:
                    nums[i] = 0
                    zeroes -= 1
                elif ones > 0:
                    nums[i] = 1
                    ones -= 1
                else:
                    nums[i] = 2
                    twos -= 1
            
            return nums

    # PYTHON BUILT-IN SOLUTION
    # def sortColors(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: None Do not return anything, modify nums in-place instead.
    #     """
    #     nums.sort()
    #     return nums