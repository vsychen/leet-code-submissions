class Solution(object):
    # TOPICS: ARRAY/BIT MANIPULATION
    # Create a list with size 32. For each element in nums, transform it into a binary representation and add to the list, each bit into one position of the list.
    # After adding all numbers to the list, mod each position by 3. For any number that appear 3 times, when that position is modded by 3, it will turn 0. As for
    # the only element that appear only one time, when modded by 3, it will remain intact. After modding each position, join them into a string again and transform
    # back into an integer.
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        v = [0]*32
        for n in nums:
            if n < 0: n += (1<<32)
            s = "{:032b}".format(n)
            for m in range(32):
                if s[m] == '1': v[m] += 1
        
        b = "".join([str(c%3) for c in v])
        if b[0] == '0': return int(b, 2)
        else: return int(b, 2) - (1<<32)