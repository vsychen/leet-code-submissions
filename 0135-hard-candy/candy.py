class Solution(object):
    # TOPICS: ARRAY/GREEDY
    # If len(ratings) is 1, return 1. Initialize a list of 1s, with the same size as ratings. First walk the list from left to right and, when the rating of the
    # child i+1 is bigger than the child i, update candies[i+1] with candies[i]+1. After finishing the walk from left to right, do the same from right to left.
    # Sum all values from the candies list and it will be the answer.
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        if len(ratings) == 1: return 1
        candies = [1]*len(ratings)

        for i in range(1, len(ratings)):
            if ratings[i-1] < ratings[i]:
                if candies[i-1] >= candies[i]:
                    candies[i] = candies[i-1]+1

        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                if candies[i] <= candies[i+1]:
                    candies[i] = candies[i+1]+1

        return sum(candies)