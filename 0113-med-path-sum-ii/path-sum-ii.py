# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # TOPICS: TREE/BINARY TREE/BACKTRACKING/DFS
    # Get all the root-to-node paths of the tree. For each path, when it reaches a leaf, check if its sum is equal to the targetSum. If it is, add to the paths list. Return the list
    # after verifying all paths.
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """
        paths = []

        def getPaths(root, lst):
            if not root: return
            elif not root.left and not root.right: 
                if sum(lst+[root.val]) == targetSum:
                    paths.append(lst+[root.val])
            else:
                if root.left:
                    getPaths(root.left, lst+[root.val])
                
                if root.right:
                    getPaths(root.right, lst+[root.val])
        
        getPaths(root, [])
        return paths