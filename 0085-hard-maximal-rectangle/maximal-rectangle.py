class Solution(object):
    # TOPICS: MATRIX/STACK
    # For each line of the matrix, apply the algorithm from the question 84 - Largest Rectangle in Histogram and save the max_area of this calculation. Update the values of the
    # list where the new value is the sum of the value in the list and the new line or 0 (if it's zero in the new line) and continue calculating max_area. Use the max value of 
    # max_area as the final answer.
    # For Reference, [Question 84 - Largest Rectangle in Histogram]'s algorithm:
    #   If there's only one element, the answer is its size. If there's only zeroes in heights, the answer is zero. If there's only one number repeated many times, the answer
    #   is its size times the length of the list. Start the stack with value -1 (it's the index correction to be applied in the index calculation) and max_area as 0. The stack
    #   should be filled with the indexes of the heights, not the heights per se. For each element in the list heights, add it to the stack if the stack is empty (only has one 
    #   element, -1) or check if the current element is less or equal than the element in the index on top of the stack; in this case, (1) get the element in the index on top of 
    #   the stack, (2) get the width of the rectangle (i - <new index on top of the stack, after the pop operation> - 1), (3) calculate the area and set the max_area as the maximum 
    #   between the current max_area value and the calculation. Repeat until there's no more indexes where its height is greater than the current value. Add the current index
    #   to the stack.
    #   When finished, the stack will be full of indexes of "heights that are less than the last position". Repeat the main algorithm with these values until the stack is empty.
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if len(heights) == 1: return heights[0]
        elif not [x for x in heights if x != 0]: return 0
        elif len(set(heights)) == 1: return heights[0]*len(heights)

        stacks = [-1]
        max_area = 0

        for i in range(len(heights)):
            while stacks[-1] != -1 and heights[i] <= heights[stacks[-1]]:
                height = heights[stacks.pop()]
                width = i-stacks[-1]-1
                max_area = max(max_area, height*width)
            stacks.append(i)
        
        while stacks[-1] != -1:
            height = heights[stacks.pop()]
            width = len(heights)-stacks[-1]-1
            max_area = max(max_area, height*width)
        
        return max_area

    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]: return 0
        elif len(matrix) == 1 and len(matrix[0]) == 1: return 0 if matrix[0][0] == "0" else 1

        aux = [0 for _ in range(len(matrix[0]))]
        max_area = 0

        for i in range(len(matrix)):
            heights = [int(matrix[i][j])+aux[j] if matrix[i][j] != "0" else 0 for j in range(len(matrix[i]))]
            max_area = max(max_area,self.largestRectangleArea(heights))
            aux = heights
        
        return max_area