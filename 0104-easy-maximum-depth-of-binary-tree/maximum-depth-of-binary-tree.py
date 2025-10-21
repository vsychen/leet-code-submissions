# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # TOPICS: TREE/BINARY TREE/DFS
    # If root is None, height is 0. If root does not have children, height is 1. For the rest of the cases, the height is the same as the maximum height from the left and right subtrees plus 1.
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root: return 0
        elif not root.left and not root.right: return 1
        else:
            return 1+max(self.maxDepth(root.left), self.maxDepth(root.right))