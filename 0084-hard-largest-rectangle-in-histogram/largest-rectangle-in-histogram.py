from itertools import groupby

class Solution(object):
    # TOPICS: ARRAY/STACK
    # If there's only one element, the answer is its size. If there's only zeroes in heights, the answer is zero. If there's only one number repeated many times, the answer
    # is its size times the length of the list. Start the stack with value -1 (it's the index correction to be applied in the index calculation) and max_area as 0. The stack
    # should be filled with the indexes of the heights, not the heights per se. For each element in the list heights, add it to the stack if the stack is empty (only has one 
    # element, -1) or check if the current element is less or equal than the element in the index on top of the stack; in this case, (1) get the element in the index on top of 
    # the stack, (2) get the width of the rectangle (i - <new index on top of the stack, after the pop operation> - 1), (3) calculate the area and set the max_area as the maximum 
    # between the current max_area value and the calculation. Repeat until there's no more indexes where its height is greater than the current value. Add the current index
    # to the stack.
    # When finished, the stack will be full of indexes of "heights that are less than the last position". Repeat the main algorithm with these values until the stack is empty.
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

    # def largestRectangleArea(self, heights):
    #     """
    #     :type heights: List[int]
    #     :rtype: int
    #     """
    #     if len(heights) == 1: return heights[0]
    #     elif not [x for x in heights if x != 0]: return 0
    #     iter = range(max(heights))
    #     stack = [0 if i >= heights[0] else (i+1) for i in iter]
    #     max_sizes = [0 if stack[i] == 0 else stack[i] for i in iter]
    #     for i in range(1, len(heights)):
    #         stack = [0 if j >= heights[i] else stack[j]+j+1 for j in iter]
    #         max_sizes = [max_sizes[j] if stack[j] <= max_sizes[j] else stack[j] for j in iter]
    #     return max(max_sizes)

    # def largestRectangleArea(self, heights):
    #     """
    #     :type heights: List[int]
    #     :rtype: int
    #     """
    #     if len(heights) == 1: return heights[0]
    #     elif not [x for x in heights if x != 0]: return 0
    #     stacks = []
    #     for i in range(max(heights)-1,-1,-1):
    #         numbers = [i+1 if heights[j] >= i+1 else 0 for j in range(len(heights))]
    #         result = [sum(group) for k, group in groupby(numbers, key=lambda x: x!= 0) if k]
    #         while stacks and stacks[-1] <= max(result):
    #             stacks.pop()
    #         stacks.append(max(result))
    #     return stacks[0]

    # def largestRectangleArea(self, heights):
    #     """
    #     :type heights: List[int]
    #     :rtype: int
    #     """
    #     if len(heights) == 1: return heights[0]
    #     elif not [x for x in heights if x != 0]: return 0
    #     areas = [[] for _ in range(max(heights))]
    #     for i in range(len(heights)):
    #         if i == 0 or heights[i] >= heights[i-1]:
    #             for j in range(heights[i]):
    #                 temp = 0
    #                 if areas[j]: temp = areas[j].pop()
    #                 areas[j].append(temp+j+1)
    #         else:
    #             for j in range(heights[i-1]):
    #                 if j < heights[i]:
    #                     temp = areas[j].pop()
    #                     areas[j].append(temp+j+1)
    #                 else:
    #                     areas[j].append(0)
    #     return max([max(x) for x in areas])

    # def getArea(self, heights, i):
    #     if heights[i] == 0: return 0
    #     if i == 0:
    #         k = i+1
    #         while k < len(heights) and heights[i] <= heights[k]: k += 1
    #         k -= 1
    #         return heights[i]*(1+k-i)
    #     elif i == len(heights)-1:
    #         j = i-1
    #         while j >= 0 and heights[i] <= heights[j]: j -= 1
    #         j += 1
    #         return heights[i]*(1+i-j)
    #     else:
    #         j = i-1
    #         while j >= 0 and heights[i] <= heights[j]: j -= 1
    #         j += 1
    #         k = i+1
    #         while k < len(heights) and heights[i] <= heights[k]: k += 1
    #         k -= 1
    #         return heights[i]*(1+k-j)
    # def largestRectangleArea(self, heights):
    #     """
    #     :type heights: List[int]
    #     :rtype: int
    #     """
    #     if len(heights) == 1: return heights[0]
    #     elif not [x for x in heights if x != 0]: return 0
    #     elif len(set(heights)) == 1: return heights[0]*len(heights)
    #     stacks = []
    #     for i in range(len(heights)):
    #         area = self.getArea(heights, i)
    #         while stacks and area >= stacks[-1]:
    #             stacks.pop()
    #         stacks.append(area)
    #     return stacks[0]