class Solution(object):
    # TOPICS: ARRAY
    # If intervals is empty, the list of intervals is [newInterval]. For each interval in intervals, check if its first value is greater than the first value of newInterval. If it is, 
    # add newInterval at that position in the intervals list. Then, for each interval check if it overlaps the following intervals. If yes, change the upper limit of the interval to
    # the maximum between the the overlapping intervals. If it does not overlaps, add the current element to the answer list and do the same for the following intervals.
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        if not intervals: return [newInterval]

        r = []
        aux = [-1,-1]
        for i in range(len(intervals)+1):
            if newInterval != [-1,-1] and i == len(intervals):
                intervals = intervals + [newInterval]
                newInterval = [-1,-1]
            elif newInterval != [-1,-1] and newInterval[0] < intervals[i][0]:
                intervals = intervals[:i] + [newInterval] + intervals[i:]
                newInterval = [-1,-1]

            if aux == [-1,-1]:
                aux = intervals[i]
            elif aux[1] < intervals[i][0]:
                r.append(aux)
                aux = intervals[i]
            else:
                aux[1] = max(aux[1], intervals[i][1])
        r.append(aux)
        return r