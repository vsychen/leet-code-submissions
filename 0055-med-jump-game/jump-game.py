class Solution(object):
    # TOPICS: ARRAY/GREEDY
    # If there's only one element in the list, it is possible to reach the end of the list. If there's no 0 in the list, it is also possible to reach the end of the list.
    # Check the first position in the list. For each checked position, check all of the next nums[i] positions as possible (or visited). At the end of the iteration, check if the last
    # position was checked. If yes, it can be reached. If not, it can't be reached.
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1: return True
        elif not [n for n in nums if n == 0]: return True
        visited = [False]*len(nums)
        visited[0] = True

        for i in range(len(nums)):
            if visited[i]:
                visited[i+1:i+1+nums[i]] = [True]*nums[i]
        return visited[-1]