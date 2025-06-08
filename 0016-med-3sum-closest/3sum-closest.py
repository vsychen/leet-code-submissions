class Solution(object):
    # TOPICS: ARRAY/TWO POINTERS
    # Sort the list of nums. Fix the middle number. Move first number up and third number down accordingly to the sum of the three numbers (if sum is less than
    # target, move first number up; if sum is greater than target, move third number down). At the same time, for each new sum, check the difference between 
    # threesum and target and save the threesum if the new difference is less than previous difference.
    # If threesum = target, answer is threesum; if none of the threesum = target, answer is the threesum that has the least difference (up or down) with target.
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