class Solution(object):
    # TOPICS: STRING/MATH
    # To multiply two numbers, first multiply its digits, then sum it all. "123" times "456" is equal to "123" times "400" plus "123" times "50" plus "123" times 6.
    # For the question requirement, it seems casting the value to integer is not allowed, so it is necessary to make the functions for sum, multiplication and comparison.
    # The method for ordering uses a list. If the first digit shows up in the list, the method returns True. Otherwise, return False. For the sum and multiplication methods,
    # two dicts are used, containing the results of up to two nines (9+9, 9*9). The results are presented as (c, d) where c is the carry and d is the digit. When adding
    # or multiplying more than one digit, if there's a carry in the less-valuable digits, it should be added to the more valuable digits.
    # Below there's also another answer to the question, but with ~indirectly~ casting the string value to integer and back.
    som = {
        "1": {"1":("0","2"),"2":("0","3"),"3":("0","4"),"4":("0","5"),"5":("0","6"),"6":("0","7"),"7":("0","8"),"8":("0","9"),"9":("1","0")},
        "2": {"2":("0","4"),"3":("0","5"),"4":("0","6"),"5":("0","7"),"6":("0","8"),"7":("0","9"),"8":("1","0"),"9":("1","1")},
        "3": {"3":("0","6"),"4":("0","7"),"5":("0","8"),"6":("0","9"),"7":("1","0"),"8":("1","1"),"9":("1","2")},
        "4": {"4":("0","8"),"5":("0","9"),"6":("1","0"),"7":("1","1"),"8":("1","2"),"9":("1","3")},
        "5": {"5":("1","0"),"6":("1","1"),"7":("1","2"),"8":("1","3"),"9":("1","4")},
        "6": {"6":("1","2"),"7":("1","3"),"8":("1","4"),"9":("1","5")},
        "7": {"7":("1","4"),"8":("1","5"),"9":("1","6")},
        "8": {"8":("1","6"),"9":("1","7")},
        "9": {"9":("1","8")}
    }
    tab = {
        "1": {"1":("0","1"),"2":("0","2"),"3":("0","3"),"4":("0","4"),"5":("0","5"),"6":("0","6"),"7":("0","7"),"8":("0","8"),"9":("0","9")},
        "2": {"2":("0","4"),"3":("0","6"),"4":("0","8"),"5":("1","0"),"6":("1","2"),"7":("1","4"),"8":("1","6"),"9":("1","8")},
        "3": {"3":("0","9"),"4":("1","2"),"5":("1","5"),"6":("1","8"),"7":("2","1"),"8":("2","4"),"9":("2","7")},
        "4": {"4":("1","6"),"5":("2","0"),"6":("2","4"),"7":("2","8"),"8":("3","2"),"9":("3","6")},
        "5": {"5":("2","5"),"6":("3","0"),"7":("3","5"),"8":("4","0"),"9":("4","5")},
        "6": {"6":("3","6"),"7":("4","2"),"8":("4","8"),"9":("5","4")},
        "7": {"7":("4","9"),"8":("5","6"),"9":("6","3")},
        "8": {"8":("6","4"),"9":("7","2")},
        "9": {"9":("8","1")},
    }

    def first(self, d1, d2):
        order = ["0","1","2","3","4","5","6","7","8","9"]
        for o in order:
            if o == d1: return True
            elif o == d2: return False

    def soma(self, d1, d2):
        if d1 == "0": return ("0",d2)
        elif d2 == "0": return ("0",d1)
        else: 
            return self.som[d1][d2] if self.first(d1, d2) else self.som[d2][d1]

    def tabuada(self, d1, d2):
        if d1 == "0" or d2 == "0": return ("0","0")
        else: return self.tab[d1][d2] if self.first(d1, d2) else self.tab[d2][d1]
    
    def multiplyByDigit(self, num, d):
        r = []
        c = "0"
        for i in range(len(num)-1,-1,-1):
            aux = c
            (c1, n1) = self.tabuada(num[i], d)
            (c2, n2) = self.soma(n1, aux)
            (_, c) = self.soma(c1, c2)
            r.append(n2)
        if c != "0": r.append(c)
        return r
    
    def sumTwoNumbers(self, num1, num2):
        # For this question, when the numbers pass through this method, their order will be reversed (ex.: ["1","2","3"] should pass here as ["3","2","1"])
        r = []
        c = "0"

        for i in range(max(len(num1), len(num2))):
            aux = c
            if i >= len(num1): 
                (c, d) = self.soma(num2[i], aux)
                r.append(d)
            elif i >= len(num2):
                (c, d) = self.soma(num1[i], aux)
                r.append(d)
            else:
                (c1, d1) = self.soma(num1[i], num2[i])
                (c2, d2) = self.soma(d1, aux)
                (_, c) = self.soma(c1, c2)
                r.append(d2)
        
        if c != "0": r.append(c)
        return r

    def sumAll(self, lst):
        r = lst[0]
        for i in range(1,len(lst)):
            r = self.sumTwoNumbers(r, lst[i])
        r.reverse()
        return "".join(r)

    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == "0" or num2 == "0": return "0"
        r = []
        num1 = list(num1)
        num2 = list(num2)
        
        for i in range(len(num2)):
            r.append(["0" for _ in range(len(num2)-i-1)] + self.multiplyByDigit(num1, num2[i]))
        return self.sumAll(r)

    # Solution below also works. The question asks to not use any BigInt, or cast string to int directly.
    # toInt = {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}
    # toStr = ["0","1","2","3","4","5","6","7","8","9"]

    # def myCastToInt(self, n):
    #     r = 0
    #     u = 0
    #     for i in range(len(n)-1,-1,-1):
    #         r += self.toInt[n[i]]*(10**u)
    #         u += 1
    #     return r
    
    # def myCastToString(self, n):
    #     r = []
    #     while n >= 10:
    #         m = n%10
    #         r.append(self.toStr[m])
    #         n = n//10
    #     r.append(self.toStr[n])
    #     r.reverse()
    #     return "".join(r)

    # def multiply(self, num1, num2):
    #     """
    #     :type num1: str
    #     :type num2: str
    #     :rtype: str
    #     """
    #     n1 = self.myCastToInt(num1)
    #     n2 = self.myCastToInt(num2)
    #     r = n1*n2
    #     return self.myCastToString(r)