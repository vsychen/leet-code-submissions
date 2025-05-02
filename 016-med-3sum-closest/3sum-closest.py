class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        r = 0
        mod_diff = 0

        for j in range(1, len(nums)-1, 1):
            i = 0
            k = len(nums)-1
            threesum = nums[i] + nums[j] + nums[k]

            if threesum == target: 
                return threesum

            while i < j and j < k:
                threesum = nums[i] + nums[j] + nums[k]
                if threesum == target:
                    return threesum
                elif threesum < target:
                    t = threesum
                    m = target - t
                    m = m if m > 0 else -m
                    if mod_diff == 0 or m < mod_diff:
                        r = t
                        mod_diff = m 
                    i += 1
                elif threesum > target:
                    t = threesum
                    m = target - t
                    m = m if m > 0 else -m
                    if mod_diff == 0 or m < mod_diff:
                        r = t
                        mod_diff = m
                        print(mod_diff)
                    k -= 1

        return r