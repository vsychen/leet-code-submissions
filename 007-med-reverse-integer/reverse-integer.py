class Solution(object):
    # TOPICS: MATH
    # Identify if the number is positive or negative. Cast the integer as a list of characters and reverse this list. If necessary, add the negative 
    # symbol ("-") again and cast this list of characters as an integer. If the number exceeds the 32-bit integer constraints, return 0 instead.
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