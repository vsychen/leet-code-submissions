class Solution(object):
    # TOPICS: MATH
    # Base case, square root of 1 is 1. While i*i <= x, double i each time until i*i is greater than x. If i*i happen to be x, return i. If not, when i*i is greater than x, divide i by 2
    # and starting from this i, add 1 until i*i is greater than x. Again, if i*i happen to be x, return i; otherwise, when i*i is greater than x, reduce one and return i.
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 1: return 1
        i = 1

        while i*i <= x:
            if i*i == x: return i
            i = i<<1
        i = i>>1

        while i*i <= x:
            if i*i == x: return i
            i += 1
        return i-1