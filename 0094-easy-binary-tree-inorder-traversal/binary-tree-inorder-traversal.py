# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    # TOPICS: STACK/TREE/DFS
    # If the tree is empty or has only one element, return it. Add the root node to the a list of nodes. Check every node in this list of nodes. If the current node
    # does not have left nor right, it's a leaf, add its value to the result list. If the node has a left node only, check if the left node was visited before. If it
    # was, add the value of the CURRENT node to the result list. If it wasn't, add the current node to be checked again later, and add the left node for verification.
    # If the current node have only right node, add the CURRENT node's value to the result list, and then add the next right node back to the list of nodes. If there
    # are left and right nodes, it's the merge of the operations from left and right: if the left node was already visited, add the CURRENT node value to the result;
    # If it was not visited yet, add the right node, the current node and the left node to the list of nodes to be visited.
    # Note: the last nodes to be visited are inserted in the list of nodes first because FILO/LIFO is being used. If FIFO was used, the order would be reversed.
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if root == None: return []
        elif not root.left and not root.right: return [root.val]

        nodes = []
        nodes.append(root)
        r = []

        while nodes:
            node = nodes.pop()
            node.visited = True

            if not node.left and not node.right:
                r.append(node.val)
            elif node.left and not node.right:
                if hasattr(node.left, "visited"): 
                    r.append(node.val)
                else:
                    nodes.append(node)
                    nodes.append(node.left)
            elif not node.left and node.right:
                r.append(node.val)
                nodes.append(node.right)
            else:
                if hasattr(node.left, "visited"):
                    r.append(node.val)
                else:
                    nodes.append(node.right)
                    nodes.append(node)
                    nodes.append(node.left)
        
        return r