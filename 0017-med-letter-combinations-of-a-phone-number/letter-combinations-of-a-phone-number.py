class Solution(object):
    # TOPICS: STRING
    # For each digit, combine the equivalent characters with the substrings received by recursion. Return all of these combinations.
    def digits(self, d):
        if d == "2": return ["a", "b", "c"]
        elif d == "3": return ["d", "e", "f"]
        elif d == "4": return ["g", "h", "i"]
        elif d == "5": return ["j", "k", "l"]
        elif d == "6": return ["m", "n", "o"]
        elif d == "7": return ["p", "q", "r", "s"]
        elif d == "8": return ["t", "u", "v"]
        elif d == "9": return ["w", "x", "y", "z"]

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0: return []
        elif len(digits) == 1: return self.digits(digits[0])
        else:
            digs = self.digits(digits[0])
            subs = self.letterCombinations(digits[1:])
            st = [d+s for s in subs for d in digs]

        return st
        