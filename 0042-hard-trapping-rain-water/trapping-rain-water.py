class Solution(object):
    # TOPICS: ARRAY/TWO POINTERS
    # The answer for this question is the same as the area of a square/rectangle minus the painted area (the painted area is the heights given by the question). The first step is to
    # know where are the square/rectangles that must be checked. The starting point of the square/rectangle is when height[i-1] is taller than height[i]. The end point is when a value
    # equal to or greater than height[i-1] appears, or when the list ends. The first case implies another height that is equal to or greater than height[i-1] exists and, in this case, 
    # the water volume trapped would be the area between the two heights minus the area that is not water (sum of the heights between the start and end points). The second case implies
    # starting point height is taller than any height until the end of the list. In this case, an "overflow of water" would occur as there's nothing to contain it from the end side of the
    # list. To solve this, call the same method, but starting from the end (this will prevent the "overflow" on the end side)
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        while height[0] < 1:
            height.pop(0)
            if len(height) <= 2: return 0
        area = 0
        i = 1

        while i < len(height):
            if height[i] < height[i-1]:
                aux = [height[i]]
                j = i+1
                while j < len(height) and height[j] < height[i-1]: 
                    aux.append(height[j])
                    j += 1
                if j < len(height): 
                    s = height[i-1]
                    e = height[j]
                    m = min(s, e)
                    r = (len(aux)*m) - sum(aux)
                else:
                    aux.reverse()
                    r = self.trap(aux+[height[i-1]])
                area += r
                i = j+1
            else:
                i += 1
        return area