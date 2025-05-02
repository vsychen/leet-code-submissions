class Solution(object):
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
