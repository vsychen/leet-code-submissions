class Solution(object):
    # TOPICS: ARRAY/DIVIDE AND CONQUER
    # If nums has only one element, maximum value would be this element. If there's two elements, return the maximum between nums[0], nums[1] and nums[0]+nums[1]. For more than two elements,
    # use Kadane's algorithm: For a list of integers, the maximum value of a sublist up to a specific point is either the value at that point, or the sum of the value at that point and 
    # the maximum value at the last position.
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1: return nums[0]
        elif len(nums) == 2: return max(max(nums), sum(nums))
        else:
            for i in range(1, len(nums)):
                nums[i] = max(nums[i], nums[i]+nums[i-1])

            return max(nums)

    # O(n) solution
    # def maxSubArray(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     max_sum = -10001
    #     aux_sum = -10001
    #     n = -10001

    #     while nums:
    #         n = nums.pop(0)

    #         if aux_sum == -10001 and n < 0:
    #             if max_sum < n: max_sum = n
    #         elif aux_sum == -10001:
    #             aux_sum = n
    #         else:
    #             if aux_sum + n < 0:
    #                 if aux_sum > max_sum:
    #                     max_sum = aux_sum
    #                 aux_sum = -10001
    #             else: 
    #                 aux_sum += n
    #         if max_sum < aux_sum: max_sum = aux_sum
    #     return max_sum