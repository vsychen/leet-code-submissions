class Solution(object):
    # TOPICS: STRING
    # Simple recursion, while counting the quantity of adjacent equal characters.
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1: return "1"
        else:
            s = self.countAndSay(n-1)
            aux = list(s)
            r = ""
            while len(aux) > 0:
                ch = aux.pop(0)
                c = 1
                while len(aux) > 0 and aux[0] == ch:
                    ch = aux.pop(0)
                    c += 1
                r += str(c) + ch
        return r