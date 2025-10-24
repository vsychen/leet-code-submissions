# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # TOPICS: TREE/BINARY TREE/DFS
    # Instead of placing the tree nodes as the right subtrees, make them the left subtrees. The pre-order traversal guarantees the correct order of the nodes. After the tree is modified
    # to only have left nodes, walk the tree again, switching the left nodes to the right, erasing the references on the left.
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        
        def to_left(root):
            if not root: return None
            elif not root.left and not root.right: return root
            else:
                far_left = to_left(root.left)

                if root.right:
                    if not far_left:
                        root.left = root.right
                    else:
                        far_left.left = root.right
                    
                    root.right = None
                    far_left = to_left(root.left)
                return far_left
        
        def to_right(root):
            if not root: return None
            elif not root.left and not root.right: return root
            else:
                to_right(root.left)
                root.right = root.left
                root.left = None
                return root
        
        to_left(root)
        to_right(root)
        return root