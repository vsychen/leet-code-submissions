# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # TOPICS: STACK/TREE/DFS/BINARY TREE
    # If the tree is empty, return an empty list. If the tree has only the root node, return a list with its value. For two or more nodes, add the root node to
    # a list to be checked and create a second list for the output. While the list to be checked is not empty, remove the first element and put its value in the
    # output list. Then, add its nodes at the start of the list to be checked (always [left node, right node, rest of the to be checked nodes]).
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root: return []
        if not root.left and not root.right: return [root.val]
        
        toCheck = [root]
        answer = []

        while toCheck:
            node = toCheck.pop(0)
            answer.append(node.val)
            if node.right:
                toCheck.insert(0, node.right)
            if node.left:
                toCheck.insert(0, node.left)
        
        return answer