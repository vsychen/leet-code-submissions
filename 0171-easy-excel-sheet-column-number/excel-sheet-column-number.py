class Solution(object):
    # TOPICS: MATH/STRING
    # Each position in the string columnTitle is equivalent to a power of 26. Insert the values of power of 26 into a powers' array where the left-most position 
    # is the most valuable power of 26 (26^len(columnTitle)-1) and the right-most position is the least valuable (26^0).
    # For each position, from 0 to len(columnTitle)-1, get the equivalent integer to the character (A=1, B=2, ...) then multiply by the corresponding value in the
    # powers' array.
    # Example: AB = 1*26^1 + 2*26^0 = 28.
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        chars = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        powers = []
        for i in range(len(columnTitle)):
            if i == 0: powers.insert(0, 1)
            else: powers.insert(0, 26*powers[0])

        count = 0
        for i in range(len(powers)):
            count += powers[i]*chars.index(columnTitle[i])
        
        return count