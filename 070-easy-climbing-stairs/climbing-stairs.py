class Solution(object):
    # TOPICS: MATH
    # It's the fibonacci sequence. Because of the question's time and memory restrictions, some changes were made to the code. Instead of using fib(x) = fib(x-1)+fib(x-2), fib(x-1)
    # was expanded so that fib(x) = (fib(x-2)+fib(x-3))+fib(x-2) = 2*fib(x-2)+fib(x-3).
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1: return 1
        elif n == 2: return 2
        elif n == 3: return 3
        else:
            return (self.climbStairs(n-2)<<1) + self.climbStairs(n-3)