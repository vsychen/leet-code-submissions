class Solution(object):
    # TOPICS: ARRAY/DYNAMIC PROGRAMMING
    # Remove any value greater than the next from the start of the list, they do not count towards the answer. After getting the first small value, search for the big values.
    # Change the big value every time it surpass the current big value. When a new smaller value appears, get the difference between the current big value and the current small
    # value and check if it's greater than the current answer and substitute if it is. Back to the big and small values, reset them and put the value as the small value, searching
    # for the next big ones. Repeat this until all the list is read. At the end, check one last time if the difference is greater than what is saved at the answer, and substitute
    # it if it is.
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        answer = 0
        mi = ma = -1

        while len(prices) > 1 and prices[0] > prices[1]:
            prices.pop(0)
        
        if len(prices) > 1:
            for i in range(len(prices)):
                if mi == -1 or (ma == -1 and prices[i] < mi):
                    mi = prices[i]
                elif prices[i] < mi:
                    if ma-mi > answer: answer = ma-mi

                    mi = prices[i]
                    ma = -1
                elif prices[i] > mi and prices[i] > ma:
                    ma = prices[i]
        
        if mi != -1 and ma!= -1 and ma-mi > answer: answer = ma-mi
        return answer