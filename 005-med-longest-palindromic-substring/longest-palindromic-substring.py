class Solution(object):
    def isPalindrome(self, s):
        l = len(s)
        for i in range(l>>1 if l>1 else l-1):
            j = len(s)-1-i
            if s[i] != s[j]:
                return False
            if i>j:
                return True
        return True

    def strip(s, c):
        i = s.index(c)
        j = s.rindex(c)+1
        return s[i:j]

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        toCheck = []
        for i in range(len(s)):
            for j in range(len(s)-1, i-1, -1):
                if s[i] == s[j]:
                    toCheck.append(s[i:j+1])
        toCheck_sorted = sorted(toCheck, key=len, reverse=True)
        for word in toCheck_sorted:
            if self.isPalindrome(word):
                return word