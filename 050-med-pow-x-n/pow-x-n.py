class Solution(object):
    # TOPICS: MATH/RECURSION
    # Power is the same as multiplying a number a number of times. However, if the exponent is too big, it could impact the calculation speed or the memory constraints. 
    # To reduce the pressure, apply the product law where x^n = (x^(n/2))*(x^(n/2)).
    # Ignoring the exponent signal, first find the value of x^(n/2). If n is even, multiply x^(n/2) by itself; if n is odd, remove one x before dividing (so n becomes even)
    # multiply x^(n/2) by itself and then multiply it by x. This way, the exponent does not become a fraction.
    # Finally, if the exponent is negative, return 1/result instead of result.
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if x == 0 or n == 0: return 1
        elif n == 1: return x
        neg = True if n < 0 else False
        n = -n if n < 0 else n

        temp_pow = self.myPow(x, n>>1)
        if n%2 == 0: r = temp_pow * temp_pow
        else: r = x * temp_pow * temp_pow
        return 1/r if neg else r