class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        r = []

        for i in range(len(nums)-2):
            if nums[i] > 0: break
            target = -nums[i]
            j = i+1
            k = len(nums)-1

            while j < k:
                if nums[j]+nums[k] == target:
                    to_add = [nums[i], nums[j], nums[k]]
                    if to_add not in r: r.append(to_add)
                    j += 1
                    k -= 1
                elif nums[j]+nums[k] > target:
                    k -= 1
                elif nums[j]+nums[k] < target:
                    j += 1
            
            # FIRST TRY SOLUTION (IS CORRECT, BUT NOT OPTIMIZED ENOUGH)
            # for j in range(i+1, len(nums)-1, 1):
            #     if self.findNum(nums[j+1:], -(nums[i]+nums[j])) != -1:
            #         to_add = [nums[i], nums[j], -(nums[i]+nums[j])]
            #         if to_add not in r: r.append(to_add)
        
        return r
