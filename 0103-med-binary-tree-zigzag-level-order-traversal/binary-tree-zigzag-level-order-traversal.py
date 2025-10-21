# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # TOPICS: TREE/BFS/BINARY TREE
    # If there's no root, return an empty list. If there's only the root node, return a matrix with only one element, the root node value. For anything else, check the list of nodes.
    # If there's at least one node, put its value in a list and append its children to a new list of nodes. After getting the information about a row, add the values to the answer list
    # and update the node list to the node children list. If there's an even number of rows in the value list, add val_row as it is. If there's an odd number of rows, add val_row in 
    # reverse. Repeat until the node list is empty.
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root: return []
        elif not root.left and not root.right: return [[root.val]]
        else:
            vals = []
            nodes = [root]

            while nodes:
                new_nodes = []
                val_row = []

                for n in nodes:
                    val_row.append(n.val)
                    if n.left: new_nodes.append(n.left)
                    if n.right: new_nodes.append(n.right)

                if val_row:
                    if len(vals) % 2 == 0:
                        vals.append(val_row)
                    else:
                        vals.append(reversed(val_row))

                if new_nodes: nodes = new_nodes
                else: nodes = []
            return vals