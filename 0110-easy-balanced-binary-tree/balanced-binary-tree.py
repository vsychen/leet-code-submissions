# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # TOPICS: TREE/BINARY TREE/DFS
    # If there's no root, the height of the tree/subtree is 0. If there's no children, but there's a root, the height of the tree/subtree is 1. For the rest of the cases, take
    # the height of the left and right subtrees. If any of them is -1, it means one of the subtrees is not balanced; return -1. If the difference between the left and right
    # subtrees' height is greater than 1, also return -1 to inform this subtree is also not balanced. For any other case, return the maximum height between the left and right
    # subtrees plus 1. At the end, just need to check if the result is different from -1. If it isn't -1, it's a balanced tree. If it is -1, it's an unbalanced tree.
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def testBalance(root):
            if not root: return 0
            elif not root.left and not root.right: return 1
            else:
                height_left = testBalance(root.left)
                height_right = testBalance(root.right)

                if height_left == -1 or height_right == -1: return -1
                elif abs(height_left-height_right) > 1: return -1
                else: return 1+max(height_left, height_right)
        return testBalance(root) != -1