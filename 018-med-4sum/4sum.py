class Solution(object):
    # ALGORITHM: BRUTE FORCE
    # Sort the list of integers. Fix the first and last numbers. While the sum of the four numbers is not equal to target, move the second number up if 
    # the sum is less than target and the third number down if the sum is greater than target. If the sum is equal to target, save the combination and 
    # check for the next numbers (move first and/or last numbers up/down, respectively).
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        r = []

        for i in range(len(nums)-3):
            for l in range(len(nums)-1, i+2, -1):
                j = i+1
                k = l-1

                while i < j and j < k and k < l:
                    foursum = nums[i] + nums[j] + nums[k] + nums[l]
                    if foursum == target:
                        to_add = [nums[i], nums[j], nums[k], nums[l]]
                        if to_add not in r: r.append(to_add)
                        j += 1
                        k -= 1
                    elif foursum > target:
                        k -= 1
                    elif foursum < target:
                        j += 1
        
        return r
