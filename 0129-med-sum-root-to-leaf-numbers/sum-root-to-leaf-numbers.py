# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # TOPICS: TREE/DFS
    # Check all paths of the tree and save the concatenation of the node values. After checking all paths, sum all of the values to get the answer.
    def sumNumbers(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def doIt(root, s):
            if not root: return [""]
            elif not root.left and not root.right: return [s+str(root.val)]
            else:
                lst = []
                if root.left:
                    lst.extend(doIt(root.left, s+str(root.val)))
                if root.right:
                    lst.extend(doIt(root.right, s+str(root.val)))
                return lst
        
        answer = 0
        for s in doIt(root, ""):
            answer += int(s)
        return answer