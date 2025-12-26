class Solution(object):
    # TOPICS: MATH/STRING
    # Get the powers of 26 in an array until the it is greater than the specified value (columnNumber). Walk through the power of 26 array from end to start
    # starting from the biggest value that is less than the specified value (columnNumber). If the specified value is bigger than the value in the power's
    # array, divide it and save the quotient in another list (track the indexes, quotient from the division by 676 should be on the second position, while
    # quotient from division by 17576 should be on the third position). For cases when columnNumber is less than the value on power's array, save the quotient
    # as 0 (zero). After getting all quotients, walk through the quotients array and, for each value less than 1 found, add 26 while reducing 1 count from the
    # next value (If the array is [25,0,3], update to [25,26,2]. If the array is [0,0,1], update to [26,-1,1], then to [26,25,0]). Reverse the array, replace
    # the integers by the corresponding letters (A-Z), then join the list into a string.
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        chars = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        powers = [1,26]
        while powers[-2]*26 <= columnNumber:
            powers.append(powers[-1]*26)

        index = [True if x > columnNumber else False for x in powers].index(True)
        answer = [0]*index

        for i in range(index-1,-1,-1):
            if columnNumber >= powers[i]:
                answer[i] = columnNumber//powers[i]
                columnNumber = columnNumber%powers[i]

        for i in range(len(answer)):
            if answer[i] < 1 and i+1 < len(answer):
                answer[i] += 26
                answer[i+1] -= 1

        return "".join([chars[c] for c in reversed(answer) if c != 0])