class Solution(object):
    # TOPICS: STRING/DYNAMIC PROGRAMMING
    # Notes: I tried it without memoization, but it did not work out.
    # If s1 or s2 is longer, return False. If (index1, index2, length) is already in memo, bring that result. Use index1 and length to get the first substring and index2 and length
    # to get the second substring. If both substrings are equal, return True. If they do not have the same composition ('aab' and 'abb', for example), return False. For each index
    # divide the strings in two and check recursively if they are scrambled. If both are scrambled, save the result as True in the memo dict. It's also possible that the current string 
    # is scrambled; in this case, it's necessary to check if the x last digits of string2 are the x first digits of string1 scrambled.
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) != len(s2): return False

        n = len(s1)
        memo = {}

        def dfs(l1, l2, length):
            if (l1, l2, length) in memo: return memo[(l1, l2, length)]

            sub1 = s1[l1:l1+length]
            sub2 = s2[l2:l2+length]

            if sub1 == sub2: return True
            elif sorted(sub1) != sorted(sub2): return False

            for i in range(1, length):
                if dfs(l1, l2, i) and dfs(l1+i, l2+i, length-i):
                    memo[(l1, l2, length)] = True
                    return True
                
                if dfs(l1, l2+length-i, i) and dfs(l1+i, l2, length-i):
                    memo[(l1, l2, length)] = True
                    return True
                
            memo[(l1, l2, length)] = False
            return False
        
        return dfs(0, 0, n)