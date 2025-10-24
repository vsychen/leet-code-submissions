"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    # TOPICS: TREE/BINARY TREE/LINKED LIST/DFS
    # If there's no root, return None. If root does not have children, return it. For the remaining cases, set the .next node of the left node as the right node. If the current
    # node has .next, also set the .next node of the right node as the left node of the current node's .next node. Recursively call the same function with the left and right nodes.
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root: return None
        elif not root.left and not root.right: return root
        else:
            root.left.next = root.right

            if root.next:
                root.right.next = root.next.left

            root.left = self.connect(root.left)
            root.right = self.connect(root.right)
            return root