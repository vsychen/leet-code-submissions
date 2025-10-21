# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # TOPICS: TREE/DFS/BINARY SEARCH TREE/BINARY TREE
    # Walk through the binary tree, passing the nodes in-order, using Morris Traversal's algorithm. Instead of printing the node's value, however, compare it with the previous in-order node.
    # Save the nodes where the values of the previous node and the in-order successor are not in an ascending order. Switch them once you finish checking the tree and the tree will be correct. 
    # O(1)
    def recoverTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        a = b = prev = prev_next = None
        r = root

        while r:
            if r.left:
                prev = r.left
                while prev.right and prev.right != r:
                    prev = prev.right

                if not prev.right:
                    prev.right = r
                    r = r.left
                else:
                    if prev_next and prev_next.val > r.val:
                        b = r
                        if not a: a = prev_next

                    prev_next = r
                    prev.right = None
                    r = r.right
            else:
                if prev_next and prev_next.val > r.val:
                    b = r
                    if not a: a = prev_next
                prev_next = r
                r = r.right

        if a and b:
            a.val, b.val = b.val, a.val

        return root

    # O(n)
    # def recoverTreeON(self, root):
    #     nodes = []
    #     values = []
    #     def dfs(root):
    #         if root.left: dfs(root.left)
    #         nodes.append(root)
    #         values.append(root.val)
    #         if root.right: dfs(root.right)
    #     dfs(root)
    #     i1 = i2 = -1
    #     for i in range(len(nodes)-1):
    #         if values[i] > values[i+1]:
    #             i1 = i
    #             break
    #     for j in range(len(nodes)-1, i1, -1):
    #         if values[j] < values[j-1]:
    #             i2 = j
    #             break
    #     nodes[i1].val = values[i2]
    #     nodes[i2].val = values[i1]
    #     return root