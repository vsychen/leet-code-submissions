class Solution(object):
    # TOPICS: ARRAY/GREEDY/TWO POINTERS
    # Start checking the area using the first and last elements from the list. If the height of the new "column" is less than the max_height, it is not necessary
    # to check the area (as the calculations started with the maximum value for length and have smaller values over time, the area will only be bigger if the 
    # height increases). Another observation is that the height used to calculate the area will be the smaller value between the two columns.
    def min(self, a, b):
        return a if a < b else b

    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_val = 0
        max_i = 0

        for i in range(len(height)):
            max_height = 0
            
            if height[i] > max_i:
                max_i = height[i]

                for j in range(len(height)-1, i, -1):
                    if max_height == 0 or height[j] > max_height:
                        area = self.min(height[i], height[j]) * (j-i)
                        max_height = height[j]
                        if area > max_val: max_val = area
                        if max_height >= height[i]: break
        
        return max_val
        