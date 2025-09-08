class Solution(object):
    # TOPICS: ARRAY/TWO POINTERS/SORTING
    # The sorting should be done in the first list and its size is fixed (there are zeroes as placeholders). Start the operation from the last position and place the greatest value
    # between the last values of the two lists (remember that the greatest element of the first list is list1[m-1], not the last). Each time the greatest value between the last elements
    # of the two lists is found, reduce that index by one. When one of the index reaches -1, that list can be considered empty, and the remaining elements of the other list should be
    # added to the merged list.
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        l = m+n
        m -= 1
        n -= 1

        for x in range(l-1, -1, -1):
            if m == -1:
                nums1[x] = nums2[n]
                n -= 1
            elif n == -1:
                nums1[x] = nums1[m]
                m -= 1
            else:
                if nums1[m] < nums2[n]:
                    nums1[x] = nums2[n]
                    n -= 1
                else:
                    nums1[x] = nums1[m]
                    m -= 1