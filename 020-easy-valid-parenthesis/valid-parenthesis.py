class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        inputs = list(s)

        while(len(inputs) > 0):
            c = inputs.pop(0)
            if len(stack) == 0 and (c == ")" or c == "]" or c == "}"): return False
            elif c == "(" or c == "[" or c == "{":
                stack.append(c)
            elif c == ")":
                if stack.pop() == "(": pass
                else: return False
            elif c == "]":
                if stack.pop() == "[": pass
                else: return False
            elif c == "}":
                if stack.pop() == "{": pass
                else: return False
            else:
                return False
        
        if len(inputs) == 0 and len(stack) > 0: return False
        return True