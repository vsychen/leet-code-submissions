class Solution(object):
    # TOPICS: ARRAY/DYNAMIC PROGRAMMING
    # First, remove useless leading and ending values (starting values too big, and ending values too low). Get the first useful value as the lower value. Walk through the list
    # noting the difference between the the lowest value and the values on the list. If there's a new lower value, substitute it. If not, get the maximum value between the last
    # number noted and the difference between the current value and the lowest value. Then, walk through the list again, this time starting from the end. Get the first value as
    # the greatest value. Walk back getting the difference between the current value and the greatest value. If a new greatest value appears, substitute it and keep going one by
    # one. Sum the elements at the same index for the two lists. The greatest value in the new list is the answer.
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        while len(prices) > 1 and prices[0] > prices[1]:
            prices.pop(0)

        while len(prices) > 1 and prices[-1] < prices[-2]:
            prices.pop()

        prices_left = []
        min_price = -1
        for i in range(len(prices)):
            if min_price == -1 or prices[i] < min_price: min_price = prices[i]
            prices_left.append(prices[i]-min_price if i == 0 else max(prices[i]-min_price, prices_left[i-1]))
        
        prices_right = []
        max_price = 1000000
        for i in range(len(prices)-1, -1, -1):
            if max_price == 1000000 or prices[i] > max_price: max_price = prices[i]
            prices_right.append(max_price-prices[i] if i == len(prices)-1 else max(max_price-prices[i], prices_right[len(prices)-2-i]))
        prices_right.reverse()
        
        answer = 0
        for i in range(len(prices)):
            if prices_left[i]+prices_right[i] > answer: answer = prices_left[i]+prices_right[i]
        
        return answer