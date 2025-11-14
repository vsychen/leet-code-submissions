class Solution(object):
    # TOPICS: STRING
    # First, remove any special characters. If the length of the string is less or equal than 1, it's a palindrome. Get the middle character. If the size of the string is odd,
    # compare the first and the reversed second half without the middle character. If they are equal, it's palindrome. If the size of the string is even, compare the first and
    # the reversed second half with the middle character. If they are equal, it's palindrome.
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = [l.lower() for l in s if l in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"]
        
        if len(s) <= 1: return True
        
        middle = len(s)>>1
        a = b = ""
        
        a = s[:middle]

        if len(s)%2 == 1:
            b = s[middle+1:]
        else:
            b = s[middle:]
        
        b.reverse()

        return a == b