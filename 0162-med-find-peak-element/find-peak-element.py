class Solution(object):
    # TOPICS: ARRAY/BINARY SEARCH
    # If there's only one element, return its index. If there are two, return the index of the biggest one. Check if the first or the last element are the peaks.
    # For all other cases, get the mid index and check against its neighbors (if it's bigger than both of its neighbors, it's a peak). If it's not, get the side
    # that is bigger than the mid index and search the sublist of that side. The reason is that, given any value, its neighbors can only have a value smaller or 
    # bigger than itself (question constraint). If the neighbors are smaller than the current value, the current value is the peak. But if any of the neighbors 
    # are bigger than the current value, it will either keep growing (and the peak will be the last element) or a smaller value will be found, and it will make 
    # that big value as the peak.
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1: return 0
        elif len(nums) == 2: return 0 if nums[0] > nums[1] else 1

        if nums[0] > nums[1]: return 0
        if nums[-1] > nums[-2]: return len(nums)-1

        def search(i, j):
            if i >= j: return
            mid = i+((j-i)>>1)
            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]: return mid
            elif nums[mid-1] >= nums[mid]: return search(i, mid)
            else: return search(mid, j)
        
        return search(0, len(nums)-1)