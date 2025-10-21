# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # TOPICS: ARRAY/BINARY TREE/DIVIDE AND CONQUER
    # The first value in the preorder list is the current node value. Search it in the inorder list to get the values that will go to the left and the values that will go to the right.
    # Repeat these steps for each node. Return the node created at each level and set it as the left/right nodes of the nodes one level above. The last node returned will be the root 
    # of the tree.
    # Note: It's extremely important to build the left subtree before the right subtree.
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        node_val = preorder.pop(0)
        val_index = inorder.index(node_val)
        to_left = inorder[:val_index]
        to_right = inorder[val_index+1:]
        left = right = None
        if to_left: left = self.buildTree(preorder, to_left)
        if to_right: right = self.buildTree(preorder, to_right)
        return TreeNode(node_val, left, right)