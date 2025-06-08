class Solution(object):
    # TOPICS: ARRAY/RECURSION/DIVIDE AND CONQUER
    # Using mergesort, merge the two sorted lists into one sorted list. If the size of this sorted list is odd, return the middle value of the list as the median.
    # If the size of this sorted list is even, sum the two middle values of the list and divide by two to have the median.
    def medianSortedArrays(self, nums1, nums2, counter, odd):
        value = -1
        if not nums1:
            value = nums2[0]
            nums2 = nums2[1:]
        elif not nums2:
            value = nums1[0]
            nums1 = nums1[1:]
        else:
            if nums1[0] <= nums2[0]:
                value = nums1[0]
                nums1 = nums1[1:]
            else:
                value = nums2[0]
                nums2 = nums2[1:]

        if counter == 0 and odd:
            return float(value)
        elif counter == 1 and not odd:
            return float((value + self.medianSortedArrays(nums1, nums2, 0, True))/2)
        else:
            return float(self.medianSortedArrays(nums1, nums2, counter - 1, odd))

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l1 = len(nums1)
        l2 = len(nums2)
        l = l1+l2
        m = int(l/2)
        print(m)
        odd = bool(l%2)

        return float(self.medianSortedArrays(nums1, nums2, m, odd))
