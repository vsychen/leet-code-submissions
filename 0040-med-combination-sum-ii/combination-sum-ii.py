class Solution(object):
    # TOPICS: ARRAY/BACKTRACKING
    # Sort the candidates list in a decreasing order and remove any values higher than the target, as they could not sum up to the target value (all values are positive)
    # Because of questions restraints, its not possible that the same element appear two times in the combination (although its possible for the value to appear two or more
    # times, if there's two or more elements with the same value). Check the entire list and see which combination sums up to the target. In case of multiple elements having
    # the same value, it is possible to shorten the time needed to check it if these elements are at the same recursion level (([2,1,1], 5) will result in [], and ([3,2,2], 5) 
    # will result in [3,2], but ([3,2,2], 7) should result in [3,2,2]).
    def findCombinations(self, candidates, target, path=[]):
        s = sum(path)
        if s == target: return [path]
        if len(candidates) == 0 or s > target: return []

        r = []
        tried = []

        for i in range(len(candidates)):
            if candidates[i] not in tried:
                tried += [candidates[i]]
                if s + candidates[i] <= target:
                    temp = path+[candidates[i]]
                    aux = self.findCombinations(candidates[i+1:], target, temp)
                    if aux != [] and aux[0] not in r: r.extend(aux)

        return r

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        candidates = sorted([c for c in candidates if c <= target], reverse=True)
        r = self.findCombinations(candidates, target)
        return r