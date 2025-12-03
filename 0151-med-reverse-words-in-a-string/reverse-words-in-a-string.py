class Solution(object):
    # TOPICS: STRING
    # Split the words using the blank space as separator. Remove the empty words. Reverse the list (last element is now first). Finally, join the words again,
    # using a single blank space as separator.
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = [w for w in s.split(" ") if w != ""]
        words = reversed(words)
        return " ".join(words)