class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 0:
            temp = list(str(x))
            temp = temp[::-1]
        else:
            temp = list(str(x)[1:])
            temp = ["-"] + temp[::-1]
        
        a = int("".join(temp))
        return a if a >= -2147483648 and a <= 2147483647 else 0