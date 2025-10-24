# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # TOPICS: TREE/BINARY TREE/BFS
    # If there's no root, the height of the tree/subtree is 0. If there's no child but there's a root, the height of the tree/subtree is 1. For any other cases, get the height from the
    # left and right subtrees. If there's any of them that is 0, return the maximum value of the heights plus 1 (the zeroed subtree does not have a leaf). If the two heights are different
    # from zero, then return the minimum value of the heights plus 1.
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root: return 0
        if not root.left and not root.right: return 1
        else:
            height_left = self.minDepth(root.left)
            height_right = self.minDepth(root.right)

            return (1+min(height_left, height_right)) if (height_left != 0 and height_right != 0) else (1+max(height_left, height_right))