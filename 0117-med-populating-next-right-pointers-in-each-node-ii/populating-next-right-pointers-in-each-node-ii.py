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
    # If there's no root, return None. If root does not have children, return it. For the remaining cases, juggle the left and right nodes, as well as the child nodes from the
    # .next node. Because it's not possible to see if the .next node has left, right or no children at all, use recursion to make the .next node decide what is the .next node to
    # be set to the current node's right-most node (the right-most node can be the left node, too). Recursively call the same function with the left and right nodes.
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        def delegate(curr):
            if not curr: return None
            elif not curr.left and not curr.right: 
                if curr.next: return delegate(curr.next)
                else: return None
            else:
                if curr.next:
                    if curr.right: curr.right.next = delegate(curr.next)
                    else: curr.left.next = delegate(curr.next)

                if curr.left and curr.right:
                    curr.left.next = curr.right
                    return curr.left
                elif not curr.right:
                    return curr.left
                else:
                    return curr.right

        if not root: return None
        elif not root.left and not root.right: return root
        else:
            delegate(root)
            self.connect(root.left)
            self.connect(root.right)
            return root