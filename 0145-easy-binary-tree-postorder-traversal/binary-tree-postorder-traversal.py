# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # TOPICS: STACK/TREE/DFS/BINARY TREE
    # If the tree is empty, return an empty list. If the tree has only the root node, return a list with its value. For two or more nodes, add the root node to
    # a list to be checked, create a second list for a stack and create a third list for the output. While the list to be checked is not empty, remove the 
    # first element of the list and check if it has children. If not, add its value to the output list. If it has, add the node to the stack as well as the 
    # current node and its children to the list to be checked (always [left node, right node, current node, rest of the nodes to be checked]).
    # When the node goes through checking again, and it's at the top of the second list (stack), add it to the answer and remove it from the stack. Walking
    # through the tree this way, the nodes will be saved in post order (left-child, right-child, current node).
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root: return []
        if not root.left and not root.right: return [root.val]
        
        toCheck = [root]
        stack = []
        answer = []

        while toCheck:
            node = toCheck.pop(0)
            if not node.left and not node.right:
                answer.append(node.val)
            else:
                if stack[-1] == node:
                    answer.append(node.val)
                    stack.pop()
                else:
                    stack.append(node)
                    toCheck.insert(0, node)

                    if node.right:
                        toCheck.insert(0, node.right)
                    if node.left:
                        toCheck.insert(0, node.left)
        
        return answer