# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # TOPICS: TREE/BINARY TREE/DFS/DYNAMIC PROGRAMMING
    # If there's only one node, return its value. Recursively visit the tree's nodes. For each child node, get the maximum isolated value and the maximum value using the child
    # node's value (bridge). For the bridge, it's the node's value added the maximum value from the left and right child nodes, if at least one of them is positive. For the 
    # isolated value, it's anything that does not concern the current node's parent node. It can be the maximum isolated value from left or right, or the bridge value from left
    # or right, or the sum of the bridge value from left, right and current node.
    # In a nutshell: (1) The isolated value won't be affected by the parent node's value, it can be directly compared with the other isolated values to get the greatest. (2) The
    # bridge value will be affected by the parent node's value; it's basically the greatest value from the current node to all of its leaves.
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root: return 0
        elif not root.left and not root.right: return root.val
        
        def pathSum(node):
            if not node: return (-1001, -1001)
            elif not node.left and not node.right: return (node.val, node.val)
            else:
                l = pathSum(node.left)
                r = pathSum(node.right)

                bridge = node.val
                if l[1] > 0 or r[1] > 0: bridge += max(l[1], r[1])

                isolated = max(l[0], r[0], l[1], r[1], l[1]+node.val+r[1])

                return (isolated, bridge)
        
        return max(pathSum(root))