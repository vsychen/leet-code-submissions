# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # TOPICS: TREE/DFS/BINARY TREE
    # Change the tree into a list and compare those lists at the end.
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        def toList(nodes, lst):
            if not [n for n in nodes if n]: return lst # Check if all nodes left to check are None
            else:
                node = nodes.pop(0)
                if node:
                    lst.append(node.val)
                    nodes.append(node.left)
                    nodes.append(node.right)
                else:
                    lst.append(None)
                return toList(nodes, lst)
        
        return toList(p) == toList(q)