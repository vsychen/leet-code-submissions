# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # TOPICS: TREE/BFS/BINARY TREE
    # For the root, just check if there are zero or two child nodes. if there aren't, return False. For zero children nodes, return True. For two, start checking the node values
    # as well as grouping the nodes to be compared together. The left-most node in the level x of the tree should be grouped with the right-most node in the same level x of the tree.
    # The left child node of the left-most node in the level x of the tree should be grouped with the right child node of the right-most node in the same level x of the tree.
    # Check the nodes in pairs, if there's not a pair, return False. After walking through the whole tree, return True if no inconsistencies were found. 
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def recursiveSymmetry(nodes):
            new_nodes = []

            if len(nodes) == 1:
                node = nodes.pop()
                if not node.left and not node.right: return True
                elif not node.left or not node.right: return False
                else:
                    new_nodes.append(node.left)
                    new_nodes.append(node.right)
                    return recursiveSymmetry(new_nodes)
            else:
                while nodes:
                    node_left = nodes.pop(0)
                    node_right = nodes.pop(0)

                    if node_left.val != node_right.val: return False

                    if not node_left.left and not node_right.right:
                        pass
                    elif not node_left.left or not node_right.right:
                        return False
                    else:
                        new_nodes.append(node_left.left)
                        new_nodes.append(node_right.right)

                    if not node_left.right and not node_right.left:
                        pass
                    elif not node_left.right or not node_right.left:
                        return False
                    else:
                        new_nodes.append(node_left.right)
                        new_nodes.append(node_right.left)

                if new_nodes: return recursiveSymmetry(new_nodes)
                else: return True
        
        def iterativeSymmetry(nodes):
            root = nodes.pop()

            if not root.left and not root.right: return True
            elif not root.left or not root.right: return False
            else:
                nodes.append(root.left)
                nodes.append(root.right)
            
            while nodes:
                node_left = nodes.pop(0)
                node_right = nodes.pop(0)

                if node_left.val != node_right.val: return False

                if not node_left.left and not node_right.right:
                    pass
                elif not node_left.left or not node_right.right:
                    return False
                else:
                    nodes.append(node_left.left)
                    nodes.append(node_right.right)

                if not node_left.right and not node_right.left:
                    pass
                elif not node_left.right or not node_right.left:
                    return False
                else:
                    nodes.append(node_left.right)
                    nodes.append(node_right.left)

            return True

        return iterativeSymmetry([root])