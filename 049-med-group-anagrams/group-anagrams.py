class Solution(object):
    # TOPICS: ARRAY/STRING
    # Base case, strs has one element; return a list with that element. Create a dictionary and use the sorted string as the key and the strings as the values for each element from strs.
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if len(strs) == 1: return [strs]

        dct = dict()
        for s in strs:
            lst = "".join(sorted(list(s)))
            if lst not in dct:
                dct[lst] = [s]
            else:
                dct[lst].append(s)
        
        return dct.values()