class MinStack(object):
    # TOPICS: STACK
    # Stack variation where operations push, pop, top and getMin need to perform in O(1) time. 

    # self.stack -> stack values
    # self.min_stack -> stack with min values
    def __init__(self):
        self.stack = []
        self.min_stack = []

    # To push values, insert the value in the stack. Then, check if min_stack is empty or if the value on top is bigger than the current value. If yes, 
    # also insert the value in the min_stack.
    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if not self.min_stack or self.min_stack[-1] > val:
            self.min_stack.append(val)

    # To pop values, pop the value on top of the stack. Compare it to the top of the min_stack. If they are the same, check if they are still present 
    # in the main stack. If they are not, pop them from the min_stack too. Doing this, the value at the top of min_stack is guaranteed to be the 
    # minimum value of the main stack, always.
    def pop(self):
        """
        :rtype: None
        """
        if self.stack.pop() == self.min_stack[-1]:
            if self.min_stack[-1] not in self.stack:
                self.min_stack.pop()

    # To peek the top value, take the value at the top of the main stack.
    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    # To peek the min value of the stack, take the value at the top of the min_stack. 
    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[-1]