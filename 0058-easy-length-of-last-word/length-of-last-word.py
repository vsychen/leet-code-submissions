class Solution(object):
    # TOPICS: STRING
    # Split the sentence with the separator " " and discard all elements that do not have anything (empty string). Get the last word and return its length.
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words = [w for w in s.split(" ") if w != '']
        return len(words[-1])