class Solution(object):
    def getLongestSubstring(self, s, charlist):
        if not s:
            return len(charlist)
        else:
            c = s[0]
            if (c in charlist):
                return len(charlist)
            else:
                return self.getLongestSubstring(s[1:], charlist+s[0])

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest = 0
        for i in range(0, len(s), 1):
            size = self.getLongestSubstring(s[i:], "")
            if size > longest:
                longest = size
            if longest == 95:
                break
        return longest