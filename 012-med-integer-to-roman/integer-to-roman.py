class Solution(object):
    def milhar(self, m):
        if m == 1: return "M"
        elif m == 2: return "MM"
        elif m == 3: return "MMM"
        else: return ""
    
    def centena(self, c):
        if c == 1: return "C"
        elif c == 2: return "CC"
        elif c == 3: return "CCC"
        elif c == 4: return "CD"
        elif c == 5: return "D"
        elif c == 6: return "DC"
        elif c == 7: return "DCC"
        elif c == 8: return "DCCC"
        elif c == 9: return "CM"
        else: return ""

    def dezena(self, d):
        if d == 1: return "X"
        elif d == 2: return "XX"
        elif d == 3: return "XXX"
        elif d == 4: return "XL"
        elif d == 5: return "L"
        elif d == 6: return "LX"
        elif d == 7: return "LXX"
        elif d == 8: return "LXXX"
        elif d == 9: return "XC"
        else: return ""

    def unidade(self, u):
        if u == 1: return "I"
        elif u == 2: return "II"
        elif u == 3: return "III"
        elif u == 4: return "IV"
        elif u == 5: return "V"
        elif u == 6: return "VI"
        elif u == 7: return "VII"
        elif u == 8: return "VIII"
        elif u == 9: return "IX"
        else: return ""

    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        m = num / 1000
        c = (num % 1000) / 100
        d = (num % 100) / 10
        u = num % 10

        return self.milhar(m) + self.centena(c) + self.dezena(d) + self.unidade(u)
        