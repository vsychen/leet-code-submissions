class Solution(object):
    # TOPICS: STRING
    # For each character of a string, check the substring that it starts. While the next character is not duplicated, continue checking the next character.
    # When a duplicated character is found, return the size of this substring and check if it is the longest yet. If yes, update the size of the longest substring.
    # Because of the questions constraints, the longest substring possible should have 95 characters, at most. If it is found, it is not necessary to continue searching.
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