class Solution(object):
    # TOPICS: ARRAY/GREEDY
    # The base cases are if the nums list is empty or have only one element. In these cases, return 0. Start the iteration by the end of the list. If its the last element of the list
    # the cost to reach the end of the list is 0. For each element of the list, check if it can reach the end of the list (or go beyond the end of the list). If yes, the cost to go to the
    # end of the list is 1. If no, get the costs of the following nums[i] elements, check the minimum cost for them and add 1. This will be the cost to get from the i element to go to the
    # end of the list. The answer is the cost at the first element of the list.
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        elif len(nums) == 1: return 0
        costs = [10000]*len(nums)
        costs[-1] = 0

        for i in range(len(nums)-1, -1, -1):
            if i+nums[i] >= len(nums)-1: costs[i] = 1
            else: 
                aux_costs = costs[i+1:i+1+nums[i]]
                costs[i] = 1+min(aux_costs) if aux_costs else 10000
        return costs[0]