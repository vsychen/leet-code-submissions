class Solution:
    # ALGORITHM: FILO/LIFO (First In, Last Out/Last In, First Out)
    # After initializing the stack, check the string for "(" and ")" chars. If "(", append its index to the stack. If ")", check if there's a corresponding "(" in the stack.
    # If there is not, update the stack index (effectively resetting the count of valid parenthesis). If there is a corresponding "(", set the difference between the current
    # index and the index of the last "invalid" parenthesis as the length of the valid parenthesis substring. If this length is greater than max_length, update it as well.
    def longestValidParentheses(self, s):
        stack = [-1]
        max_length = 0

        for i, char in enumerate(s):
            print(i, char)
            if char == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_length = max(max_length, i - stack[-1])
                print(stack)
        
        return max_length
    
    # def rindex(self, lst, value):
    #     lst.reverse()
    #     i = lst.index(value)
    #     lst.reverse()
    #     return len(lst) - i - 1

    # def longestValidParentheses(self, s):
    #     """
    #     :type s: str
    #     :rtype: int
    #     """
    #     s = s.lstrip(")")
    #     s = s.rstrip("(")

    #     if len(s) == 0: return 0

    #     stack = []
    #     array = []

    #     for i in range(len(s)):
    #         if s[i] == "(":
    #             stack.append(s[i])
    #             array.append("0")
    #         else:
    #             if len(stack) > 0:
    #                 array[self.rindex(array, "0")] = "1"
    #                 array.append("1")
    #                 stack.pop()
    #             else:
    #                 array.append("0")

    #     longest = len(sorted(("".join(array)).split("0"), key=len, reverse=True)[0])
    #     return longest