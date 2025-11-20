class Solution(object):
    # TOPICS: ARRAY/BIT MANIPULATION
    # If len(nums) is 1, return the only element as answer. For anything else, use XOR (bit manipulation) to reduce the list. The final value will be the answer.
    # XOR works in a way that if it's applied two times with the same arguments, it will turn back to the initial value. So, with a list [1,2,2], the value of the
    # variable will be 1 (01) -> 3 (11) -> 1 (01), the only single element in the list, no matter the order.
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1: return nums[0]
        else:
            v = nums.pop(0)
            for n in nums:
                v = v^n
            return v

    # Another way to solve the question is to remove the first element and then use that element to remove by value. If an error is found, that's the answer.
    # Otherwise, keep removing until there's only one element left. This solution, however, is cost more than O(n); in the worst case, it will need to do walk
    # through the list n/2 times, with an O(m) cost for each .remove(), with m=n at the start and m decreasing by two after each iteration.
    # def singleNumber(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     if len(nums) == 1: return nums[0]
    #     else:
    #         v = None
    #         try:
    #             while not v or len(nums) > 1:
    #                 v = nums.pop(0)
    #                 nums.remove(v)
    #             if len(nums) == 1: return nums[0]
    #         except Exception:
    #             return v