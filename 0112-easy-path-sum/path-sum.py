# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # TOPICS: TREE/BINARY TREE/DFS
    # Get all the root-to-node paths of the tree into a list. For each element of the list (a path), sum all of its values; if their sum is equal to the targetSum, return True.
    # If no path sum is equal to the targetSum, return False.
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        paths = []

        def getPaths(root, lst):
            if not root: return
            elif not root.left and not root.right: paths.append(lst+[root.val])
            else:
                if root.left:
                    getPaths(root.left, lst+[root.val])
                
                if root.right:
                    getPaths(root.right, lst+[root.val])
        
        getPaths(root, [])

        for path in paths:
            if sum(path) == targetSum: return True
        
        return False