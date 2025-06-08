class Solution(object):
    # TOPICS: STRING/RECURSION
    # Split the pattern into tokens - specific character (a), wildcard character (.), zero or more specific characters (*a) and zero or more wildcard characters (*.).
    # Changed the order of the "zero or more character" for convenience (a* -> *a; .* -> *.)
    # Simplified the tokens (if the pattern is *a*., this is the same as *. because *a can be ZERO or more. similarly, *a*a is the same as *a).
    # Match tokens with string. Basecase: (1) if the length of the string is 0 and length of tokens is zero, string matches pattern; (2) if length of the string is 
    # not zero and length of tokens is zero, string does not matches the pattern. (3) if length of the string is zero but the length of the tokens is not zero, 
    # check if the remaining tokens are "zero or more" tokens to decide if string matches pattern.
    # If token is not "zero or more", match the current character with the token. If matches, go to next character/token.
    # If token is "zero or more specific characters", need to check if any of the strings containing this specific character matches the pattern
    # (aaab -> check if any of <aaab, aab, ab, b> matches the rest of the pattern)
    # If token is "zero or more wildcard characters", need to check if any of the following strings matches the pattern.
    # (abcd -> check if any of <abcd, bcd, cd, d> matches the rest of the pattern)
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