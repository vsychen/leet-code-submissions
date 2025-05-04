class Solution(object):
    # ALGORITHM: MODIFIED BRUTE FORCE
    # Multiply the divisor by 2 until it is greater than dividend. Divide the divisor by 2 one time. This forces the divisor to be less than, or equal to the dividend.
    # If equal, return the quocient. If almost equal [((quocient-1)*divisor) < dividend < (divisor*quocient)], return quocient-1 (truncate towards zero).
    # Recursively call the method (instead of finding the quocient by doing "-x/+x" operations, it is more cost-effective to do "-y/+y" operations, where y is 2^z).
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        signal = True
        if dividend < 0: 
            dividend = -dividend
            signal = not signal
        if divisor < 0: 
            divisor = -divisor
            signal = not signal
        
        q = 1
        if divisor == 1: q = dividend
        elif divisor > dividend: q = 0
        elif divisor == dividend: q = 1
        else:
            temp = divisor
            while temp < dividend:
                temp = temp << 1
                q = q << 1
            
            if temp == dividend:
                temp >> 1
                q >> 1
            else:
                if temp - divisor < dividend: q -= 1
                else:
                    temp -= dividend
                    q -= self.divide(temp, divisor)
                    q -= 1

        if q > 2147483647 and not signal: q = 2147483648
        elif q > 2147483647 and signal: q = 2147483647

        return q if signal else -q