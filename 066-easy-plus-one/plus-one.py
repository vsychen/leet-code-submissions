class Solution(object):
    # TOPICS: ARRAY/MATH
    # Reverse the digits list. If the first digit is not 9, just add 1 to it and return its reverse again. If the first digit is 9, make it 0 and add 1 to the carry digit.
    # While the carry digit is 1 and is not the end of the list, check if the digits is 9 or not. If not, just add 1 to it and change the carry digit to 0 to end the loop and return the
    # reverse of the list. If the list is full of 9's, at the end of the loop, the list will turn from 9...9 to 0...0; just add 1 to the end of the list, making it 0...01 and reverse it,
    # making it 10...0.
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits = digits[::-1]
        if digits[0] != 9:
            digits[0] += 1
        else:
            c = 1
            digits[0] = 0

            i = 1
            while i < len(digits) and c == 1:
                if digits[i] != 9:
                    c = 0
                    digits[i] += 1
                else:
                    digits[i] = 0
                    i += 1
            if c == 1: digits.append(1)
        return digits[::-1]