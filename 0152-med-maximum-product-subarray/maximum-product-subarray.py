class Solution(object):
    # TOPICS: ARRAY/DYNAMICS PROGRAMMING
    # Walk through the list of nums recording two values, one min and one max, between the product at the previous position and the current number and
    # the de facto current number (the de facto comparation will be between two products, as each position in the products list has two values, and 
    # the current nums[i]) It's necessary to save both the largest and the smalles value because, in the next multiplications there's a chance to 
    # multiply the current value by a negative value, essentially turning the smallest value into the biggest as well as the reverse situation.
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        answer = [None]*len(nums)
        for i in range(len(nums)):
            if i == 0:
                answer[i] = (nums[i], nums[i])
            else:
                answer[i] = (min(answer[i-1][0]*nums[i], nums[i], answer[i-1][1]*nums[i]), max(answer[i-1][0]*nums[i], nums[i], answer[i-1][1]*nums[i]))

        return max([n for m in answer for n in m])