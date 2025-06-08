class Solution(object):
    # TOPICS: ARRAY
    # First, sort the intervals array using the first element as the key. For each element, check if it overlaps with the next elements. If yes, change the upper limit of the interval to
    # the maximum between the elements. If it does not overlap, add the current element to the answer list and start checking the next element.
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals = sorted(intervals, key=lambda x: x[0])
        r = []
        aux = [-1,-1]
        for i in intervals:
            if aux == [-1,-1]:
                aux = i
            elif aux[1] < i[0]:
                r.append(aux)
                aux = i
            else:
                aux[1] = max(aux[1], i[1])
        r.append(aux)
        return r