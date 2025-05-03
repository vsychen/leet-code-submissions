class Solution(object):
    # ALGORITHM: MODIFIED BRUTE FORCE/PYTHON TIMSORT (MERGESORT+INSERTIONSORT)
    # First, add all strings that start and end with same character in a list and sort this list in a reverse order (the longest string will then be the first element)
    # Check if the words are palindrome. If one palindrome is found, return it as the answer (it will necessarily be the longest palindrome because of the sort)
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