class Solution(object):
    # TOPICS: ARRAY/BINARY SEARCH
    # Walk through the list picking the element in the position i as the first element. Get the second
    # value needed subtracting numbers[i] from the target value. If the second value needed is the same
    # as numbers[i], check the adjacent values (numbers[i-1] and numbers[i+1]). If both are different
    # than numbers[i], discard the possibility and go for another value. Use binary search to find the
    # needed value in the list to the left/right of i. When the value of the second index is different
    # than -1, the binary search found the value in the list. Return these two index sorted.
    # To help reduce runtime, a variable prev was used. After checking one number 'x', if 'target-x'
    # is not found, there's no need to keep searching for 'target-x'. Skip the rest of 'x' and go for
    # the next possible value.
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        r = None
        if target >= 0: r = range(len(numbers)-1,-1,-1)
        else: r = range(len(numbers))

        def find(i, j, n):
            if i >= j: return -1
            mid = (i+j)>>1
            if numbers[mid] == n: return mid
            elif numbers[mid] > n: return find(i, mid, n)
            else: return find(mid+1, j, n)

        prev = -1001
        for i in r:
            if numbers[i] != prev:
                n2 = target-numbers[i]
                if n2 == numbers[i]:
                    if i > 0 and numbers[i-1] == n2: return [i, i+1]
                    elif i < len(numbers)-1 and numbers[i+1] == n2: return [i+1, i+2]

                i2 = -1
                if n2 < numbers[i]: i2 = find(0, i, n2)
                else: i2 = find(i+1, len(numbers)-1, n2)

                if i2 != -1: return [min(i, i2)+1, max(i, i2)+1]
                prev = numbers[i]