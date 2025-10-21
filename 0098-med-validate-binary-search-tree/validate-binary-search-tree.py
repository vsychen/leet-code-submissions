# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # TOPICS: TREE/DFS/BST/BINARY TREE
    # Check the nodes using DFS. If there's no duplicates and the list printed by the DFS is ordered, it's a valid BST. Otherwise, it's not.
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        r = []
        def dfs(root):
            if root.left: dfs(root.left)
            r.append(root.val)
            if root.right: dfs(root.right)

        dfs(root)

        return len(r) == len(set(r)) and r == sorted(r)
