class Solution(object):
    # TOPICS: STRING
    # Sort the strings by the size and get the longest one. For each of the other strings, check which characters are common to both base_string and the current string.
    # The answer will be any characters before "" in the base_string list of characters ("" means the character was not present in that position in some strings)
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        base_string = list(sorted(strs, key=len)[0])

        for s in strs:
            to_check = list(s)
            for c in range(len(base_string)):
                if base_string[c] == "": pass
                elif c >= len(to_check): base_string[c] = ""
                elif base_string[c] != to_check[c]: base_string[c] = ""
                else: pass
        
        r = ""
        temp_index = 0
        while temp_index < len(base_string) and base_string[temp_index] != "":
            r += base_string[temp_index]
            temp_index += 1
        
        else: return r
