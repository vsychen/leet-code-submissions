class Solution(object):
    # TOPICS: ARRAY/SORTING
    # Sort the list in O(n). Then walk through the sorted list checking adjacent elements to get the biggest gap and return it as the answer.
    #
    # Sorting algorithm used: Radix Sort.
    # 1. Find the max number of iterations (length of the biggest number, length as in string length)
    # 2. For each iteration (i=length-1 -> i=0):
    #    2.1. Create a list of buckets representing each digit from 0 to 9. (auxiliary list)
    #    2.2. Walk through the list of stringified numbers getting the number at position i (units, tens, hundreds, etc.) from less valuable to most valuable:
    #         2.2.1. Use the number at position i to determine to which bucket the stringified number will be added to.
    #    2.3. After each shuffle, change the stringified list to a concatenation of the auxiliary list's buckets.
    # 3. At the end of the iterations, the stringified list will be sorted. Cast its elements back into integer and return as the output.
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def sortInON(lst):
            l = len(str(max(lst)))
            str_lst = [str(n).zfill(l) for n in lst]

            for i in range(l-1,-1,-1):
                aux = [[] for _ in range(10)]

                for j in range(len(str_lst)):
                    c = int(str_lst[j][i])
                    aux[c].append(str_lst[j])
                str_lst = [e for a in aux for e in a]

            return [int(s) for s in str_lst]

        nums = sortInON(nums)
        gap = 0
        for i in range(1, len(nums)):
            diff = nums[i]-nums[i-1]
            if gap < diff:
                gap = diff
        
        return gap