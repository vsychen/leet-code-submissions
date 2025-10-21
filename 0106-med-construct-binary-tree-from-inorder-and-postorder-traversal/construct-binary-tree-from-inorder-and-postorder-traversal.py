# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # TOPICS: ARRAY/BINARY TREE/DIVIDE AND CONQUER
    # The last value in the postorder list is the current node value. Search it in the inorder list to get the values that will go to the left and the values that will go to the right.
    # Repeat these steps for each node. Return the node created at each level and set it as the right/left nodes of the nodes one level above. The last node returned will be the root 
    # of the tree.
    # Note: It's extremely important to build the right subtree before the left subtree.
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        node_val = postorder.pop()
        val_index = inorder.index(node_val)
        to_left = inorder[:val_index]
        to_right = inorder[val_index+1:]
        left = right = None
        if to_right: right = self.buildTree(to_right, postorder)
        if to_left: left = self.buildTree(to_left, postorder)
        return TreeNode(node_val, left, right)