class Solution(object):
    # TOPICS: STRING/SLIDING WINDOW
    # For the base cases, if s = t, the answer is s; if t has more characters than s, the answer is ""; if there's a character in t, but s does not
    # contain it, the answer is "". Make a dictionary with all characters in t, where the value is the count of the key in t. In s, search for the first
    # substring that contains all of the characters in t, i.e., when all keys in the dict have values less or equal than 0. Move the left index up while
    # s[i] is not in the dictionary or s[i] is less than 0 in the dictionary, they are not part of the minimum window. After finding the first window
    # with all characters in t, move it up in the string s and if there's a substring with all characters in t, but smaller than the current substring,
    # update the answer.
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if s == t: return s
        elif not t or len(s) < len(t): return ""
        elif [x for x in t if x not in s]: return ""

        tokens = { k:list(t).count(k) for k in list(t) }
        i = 0
        while s[i] not in tokens: i += 1
        j = i+len(t)
        if j > len(s): return ""
        for c in s[i:j]:
            if c in tokens: tokens[c] -= 1

        while [v for v in tokens.values() if v > 0]:
            if j >= len(s): return ""
            elif s[j] in tokens: tokens[s[j]] -= 1
            j += 1

        while i<len(s) and (s[i] not in tokens or tokens[s[i]] < 0):
            if s[i] in tokens: tokens[s[i]] += 1
            i += 1

        min_length = j-i
        answer = s[i:j]

        while i<len(s) and j<len(s):
            while j<len(s) and s[j] != s[i]:
                if j<len(s) and s[j] in tokens: tokens[s[j]] -= 1
                j += 1
            if j<len(s) and s[j] == s[i]: tokens[s[j]] -= 1
            j += 1

            while i<len(s) and (s[i] not in tokens or tokens[s[i]] < 0):
                if s[i] in tokens: tokens[s[i]] += 1
                i += 1

            if j-i < min_length:
                min_length = j-i
                answer = s[i:j]
        
        return answer