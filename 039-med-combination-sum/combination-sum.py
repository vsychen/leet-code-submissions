class Solution(object):
    # ALGORITHM: BRUTE FORCE
    # Sort the candidates in a descending order. For each candidate, check if it is less than or equal to the target. If equal to target, add it to the answer and verify the next
    # combination.
    # Observation: for input ([1,2,3], 5), both [3,2] and [3,1,1] are valid and should be in the answer. Need to continue checking the combinations of [3, ...] even after [3,2] 
    # is found.
    def comb(self, candidates, curr, target):
        if len(candidates) == 0: 
            return [curr] if sum(curr) == target else []
        else:
            if sum(curr) == target:
                return [curr]
            elif sum(curr) > target:
                return []
            else:
                r = []
                for i in range(len(candidates)):
                    if sum(curr) + candidates[i] <= target:
                        temp = curr + [candidates[i]]
                        aux = self.comb(candidates[i:], temp, target)

                        if aux != [] and aux not in r: r += aux

                return r

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = sorted([c for c in candidates if c <= target], reverse=True)
        r = (self.comb(candidates, [], target))

        return r