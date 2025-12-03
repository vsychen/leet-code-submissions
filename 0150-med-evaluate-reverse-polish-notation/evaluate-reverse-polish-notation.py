class Solution(object):
    # TOPICS: STACK
    # If tokens has one element, the answer is it's value. For more than one element, start pushing the elements into a stack if they are numbers. If they
    # operators (+, -, *, /), pick two elements from the stack and use them to perform the operation (the first element removed is the second term, as the
    # order can affect the result for subtraction and division) and then put the result back into the stack.
    # After all the operations, the number remaining inside the stack is the result of the equation.
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        if len(tokens) == 1: return int(tokens[0])

        stack = []
        while tokens:
            c = tokens.pop(0)
            if c in "+-*/":
                n2 = stack.pop()
                n1 = stack.pop()

                if c == "+": stack.append(n1+n2)
                elif c == "-": stack.append(n1-n2)
                elif c == "*": stack.append(n1*n2)
                # elif c == "/": stack.append(int(n1/n2)                 # This does not work on LeetCode.
                elif c == "/": stack.append(int(n1/float(n2)))           # This is the solution to work on LeetCode.
            else:
                stack.append(int(c))
        
        return stack[0]