class Solution(object):
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