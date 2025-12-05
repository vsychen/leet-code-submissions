class Solution(object):
    # TOPICS: ARRAY/MATH
    # If there are 2 or less points in the input, return the number of points as the answer. To know if three points are inline, calculate the cross product of
    # the two resulting vectors (x->y and y->z). If their cross product is 0, they are colinear. Fix two points and the other points with the two fixed. Count
    # how many points have cross product equal to 0 when paired with the fixed ones. Do the same for all combinations of two points x and y, returning the 
    # largest amount of points where the cross product is 0.
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if len(points) <= 2: return len(points)
        
        def isLine(p1, p2, p3):
            x1,x2 = p2[0]-p1[0],p2[1]-p1[1]
            y1,y2 = p3[0]-p2[0],p3[1]-p2[1]
            return (x1*y2-x2*y1)==0

        def checkPoints(p1, p2, points):
            validPoints = [p for p in points if isLine(p1, p2, p)]
            return 2+len(validPoints)
        
        max_points = 0
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                p1 = points[i]
                p2 = points[j]
                aux = checkPoints(p1, p2, points[j+1:])
                if aux > max_points: max_points = aux
        
        return max_points