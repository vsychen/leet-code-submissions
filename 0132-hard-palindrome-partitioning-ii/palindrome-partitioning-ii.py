class Solution(object):
    # TOPICS: MATRIX/DYNAMIC PROGRAMMING
    # Pre-compute the palindrome words: (1) words of one character are always palindromes. (2) two characters are palindromes when both characters are the same.
    # (3) for words of three or more characters, see if the two outwards characters (left-most and right-most) match and then check the matrix for the rest of
    # the word.
    # Make a list of integers with lst[i] representing how many cuts are needed to solve the question for s[:i+1]. Walk through the list with two pointers, the
    # first one representing the index mentioned just before (i.e. 'i' represent how many cuts are needed to solve the question for s[:i+1]) and the second one
    # checking all possibilities until i+1 (i.e. [0:i], [1:i], ..., [i:i]). If the substring is a palindrome, lst[i] is 0 if j == 0, or it's the minimum between
    # lst[i] and lst[j-1]+1 (i.e. the minimum value between the current value and the value from the start of the palindrome plus one cut).
    # Return the value of the last position of the list as the answer.
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        size = len(s)
        if s == s[::-1]: return 0
        isPalindrome = [[False]*size for _ in range(size)]

        for i in range(size):
            isPalindrome[i][i] = True
        for i in range(size-1):
            isPalindrome[i][i+1] = s[i] == s[i+1]
        for length in range(3, size+1):
            for i in range(size-length+1):
                j = i+length-1
                isPalindrome[i][j] = (s[i] == s[j]) and isPalindrome[i+1][j-1]

        lst = [2001]*size
        for i in range(size):
            for j in range(i+1):
                if isPalindrome[j][i]:
                    if j == 0: lst[i] = 0
                    else: lst[i] = min(lst[i], lst[j-1]+1)

        return lst[-1]