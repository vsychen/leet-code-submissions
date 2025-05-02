class Solution(object):
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
        