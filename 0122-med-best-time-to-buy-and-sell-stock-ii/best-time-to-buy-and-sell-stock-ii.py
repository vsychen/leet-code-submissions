class Solution(object):
    # TOPICS: ARRAY/DYNAMIC PROGRAMMING
    # Remove any value greater than the next from the start of the list, they do not count towards the answer. After getting the first small value, search for the big values.
    # Change the big value every time it surpass the current big value. When a new smaller value appears, get the difference between the current big value and the current small
    # value and sum it to the answer (profit). Reset the big and small values and put the new value as the small value, before resuming the search for the big values. 
    # Repeat this until all the list is read. At the end, sum the difference between the small and big value one last time if both of them are valid (greater than -1).
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        answer = 0
        mi = ma = -1
        prev = -1

        while len(prices) > 1 and prices[0] > prices[1]:
            prices.pop(0)
        
        if len(prices) > 1:
            for i in range(len(prices)):
                if mi == -1 or (ma == -1 and prices[i] < mi):
                    mi = prices[i]
                elif prices[i] < prev:
                    answer += ma-mi
                    mi = prices[i]
                    ma = -1
                elif prices[i] > mi and prices[i] > ma:
                    ma = prices[i]
                prev = prices[i]
        
        if mi != -1 and ma!= -1: answer += ma-mi
        return answer