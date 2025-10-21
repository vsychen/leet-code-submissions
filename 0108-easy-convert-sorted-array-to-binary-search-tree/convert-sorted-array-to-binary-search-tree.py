# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # TOPICS: ARRAY/BINARY SEARCH TREE/DIVIDE AND CONQUER
    # Base cases: (1) if nums is empty, return None; (2) if nums has only one element, return a leaf node with this element as value.
    # For anything else, get the middle value from the number list and set it as the current node's value. Any value to the left, recursively call the method to build the left subtree;
    # anything to the right, recursively call the method to build the right subtree. 
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        if not nums: return None
        elif len(nums) == 1: return TreeNode(nums[0])

        mid_index = len(nums) >> 1
        left = nums[:mid_index]
        right = nums[mid_index+1:]

        return TreeNode(nums[mid_index], self.sortedArrayToBST(left), self.sortedArrayToBST(right))