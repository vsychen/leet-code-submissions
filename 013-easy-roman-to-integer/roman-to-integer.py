class Solution(object):
    # ALGORITHM: NONE
    # Get each character and transform it in an integer to sum to the total value. If the character have greater value than the previous one, it is necessary to
    # subtract two times of the previous character to compensate the previous adding (IX -> Add 1 -> Add 10 -> Subtract 2 -> Total 9)
    def translate(self, c):
        if c == "M": return 1000
        elif c == "D": return 500
        elif c == "C": return 100
        elif c == "L": return 50
        elif c == "X": return 10
        elif c == "V": return 5
        elif c == "I": return 1
        else: return 0

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum = 0
        old_value = 0
        value = 0

        for i in range(len(s)):
            old_value = value
            value = self.translate(s[i])

            if value > old_value:
                sum += value - (old_value << 1)
            else:
                sum += value
        
        return sum
        