class Solution(object):
    # TOPICS: MATH/STRING/BIT MANIPULATION
    # Reverse both a and b, and set a variable for the carry bit. For each position, if there's not a bit in a or in b, check the combination between the bit of the remaining string and
    # the carry bit and save the value of the "sum" and the new carry bit (0+0->00; 0+1->01; 1+0->01; 1+1->10). If both a and b have bits in that position, check the combination between
    # the two bits in addition to the carry bit and save the value of the "sum" and the new carry bit (0+0+0->00; 0+0+1->01; 0+1+0->01; 0+1+1->10; 1+0+0->01; 1+0+1->10; 1+1+0-> 10;
    # 1+1+1->11). If at the end of the sum, the carry bit is equal to "1", append it to the end of the list, reverse the result list and return it as the answer.
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = a[::-1]
        b = b[::-1]
        z = False
        r = []

        for i in range(max(len(a), len(b))):
            if i >= len(a): 
                y = (b[i] == "1")
                r.append("1" if y^z else "0")
                z = y and z
            elif i >= len(b):
                x = (a[i] == "1")
                r.append("1" if x^z else "0")
                z = x and z
            else:
                x = (a[i] == "1")
                y = (b[i] == "1")
                r.append("1" if (not z and (((not x) and y) or (x and (not y)))) or (z and ((x and y)^(not x and not y))) else "0")
                z = (x and (y^z)) or (y and z)
        
        if z: r.append("1")
        return "".join(r[::-1])