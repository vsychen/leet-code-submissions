class Solution(object):
    # ALGORITHM: LIFO/FILO (Last In, First Out / First In, Last Out)
    # Check all characters of the list. If character is open type "(", "[" or "{", add to the stack. If the character is close type ")", "]" or "}", remove from stack
    # if it matches the top of the stack (in Python, the last position of the list). Ex.: Add "(" to stack -> Rem "]" from stack -> NOT VALID COMBINATION
    # At the end, check if the input and the stack is empty. If any of them are not, the string is not valid.
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