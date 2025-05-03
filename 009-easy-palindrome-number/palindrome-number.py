class Solution(object):
    # ALGORITHM: NONE
    # Cast the integer as a list of characters. Reverse the list of characters. Compare the two strings.
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s1 = list(str(x))
        s2 = s1[::-1]
        return s1==s2