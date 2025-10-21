class Solution(object):
    # TOPICS: ARRAY/BACKTRACKING/BIT MANIPULATION
    # Sort the nums list. Get the length of nums. The maximum number of combinations will be 2^length(nums). Consider all binary combinations from 0 to (2^length(nums))-1.
    # For each combination, put the numbers that correspond to '1' together and add to the result set. After considering all combinations, return the result set as answer.
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        nums_length = len(nums)
        result_size = pow(2, nums_length)
        result = []

        for x in range(result_size):
            clue = "{:010b}".format(x)[10-nums_length:]
            print(clue)
            temp = [nums[i] for i in range(len(nums)) if clue[i] != '0']
            if temp not in result: result.append(temp)

        return result