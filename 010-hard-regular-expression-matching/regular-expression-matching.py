class Solution(object):
    def getTokens(self, p):
        temp = list(p)
        for i in range(len(temp)):
            if temp[i] == "*":
                temp[i-1] = "*" + temp[i-1]
                temp[i] = ""

        return [temp[j] for j in range(len(temp)) if temp[j] != ""]
    
    def simplify(self, p):
        stack = []
        result = []

        for i in range(len(p)):
            # print(i, p, stack)
            if p[i] == "*.":
                stack = ["*."]
            elif p[i][0] == "*":
                if len(stack) == 0: stack.append(p[i])
                elif stack[-1] == "*." or stack[-1] == p[i]: pass
                else: stack.append(p[i])
            elif "*" not in p[i]:
                result += stack
                result.append(p[i])
                stack = []
        
        result += stack
        # print(result)
        return result

    def matchTokens(self, s, tokens):
        # print("START", s, tokens)
        if len(s)==0 and len(tokens)==0:
            return True
        elif len(s)==0 and len(tokens)!=0:
            temp = [t for t in tokens if "*" not in t]
            return False if len(temp)>0 else True
        elif len(s)!=0 and len(tokens)==0:
            return False

        token = tokens[0]
        if token == "*.":
            # print("TOKEN .*", s, tokens)
            if len(tokens) == 1: return True
            tokens.pop(0)
            token = tokens[0]
            m = False

            if token != ".":
                while len(s) > 0 and s[0] != token:
                    s = s[1:]
                
                if len(s) == 0: return False
                elif len(s) == 1 and len(tokens) == 1: return True
                else:
                    while len(s) > 0 and not m:
                        m = self.matchTokens(s, tokens)
                        if m: print("TRUE", s, tokens)
                        s = s[1:]
            else:
                while len(s) > 0 and not m:
                    m = self.matchTokens(s, tokens)
                    if m: print("TRUE", s, tokens)
                    s = s[1:]

            if m: return True
            elif len(s) == 0 and len(tokens) != 0: return True if len([t for t in tokens if "*" not in t]) == 0 else False
            else: return False
        elif "*" in token:
            # print("TOKEN A*", s, tokens)
            if len(tokens) == 1: return True if s.replace(token[1], "") == "" else False
            if s[0]!=token[1]: # abc d*abc d tem 0 correspondencias
                return self.matchTokens(s, tokens[1:])
            else:
                m = False
                while len(s) > 0 and s[0] == token[1] and not m:
                    m = self.matchTokens(s, tokens[1:])
                    if m: print("TRUE", s, tokens)
                    s = s[1:]

                if m: return True
                elif len(s) == 0 and len(tokens) == 0: return True
                elif len(s) == 0 and len(tokens) != 0: return True if len([t for t in tokens if "*" not in t]) == 0 else False
                elif len(s)!=0 and len(tokens)!=0: return self.matchTokens(s, tokens[1:]) # não é s[1:] pq ja tirei o caracter no loop anterior
                else: return False
        elif token == ".":
            # print("TOKEN .", s, tokens)
            return self.matchTokens(s[1:], tokens[1:])
        else:
            # print("TOKEN A", s, tokens)
            if token != s[0]: return False
            return self.matchTokens(s[1:], tokens[1:])

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        return self.matchTokens(s, self.simplify(self.getTokens(p)))