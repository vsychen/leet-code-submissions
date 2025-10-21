from itertools import permutations

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    # TOPICS: DYNAMIC PROGRAMMING/BACKTRACKING/TREE/BINARY SEARCH TREE/BINARY TREE
    # Generate a list of permutations of a list from 1 to n. For each of these permutations, insert the elements in order into a tree (if there are n permutations, there will be
    # n trees). While adding the trees to the answer list, it's necessary to check if there are duplicates. To check for duplicates, transform the tree into a list to be able
    # to compare them. Only add unique trees to answer.
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[Optional[TreeNode]]
        """
        if n == 1: return [TreeNode(1, None, None)]

        def createTree(lst):
            root = None

            def insertNode(root, val):
                if root == None: return TreeNode(val, None, None)
                else:
                    if root.val > val:
                        root.left = insertNode(root.left, val)
                    else:
                        root.right = insertNode(root.right, val)
                    return root

            for i in range(len(lst)):
                root = insertNode(root, lst[i])
            
            return root

        def toList(nodes, lst):
            if not [n for n in nodes if n]: return lst # Check if all nodes left to check are None
            else:
                node = nodes.pop(0)
                if node:
                    lst.append(node.val)
                    nodes.append(node.left)
                    nodes.append(node.right)
                else:
                    lst.append(None)
                return toList(nodes, lst)

        r = []
        aux = []
        for l in permutations([i for i in range(1, n+1)]):
            tree = createTree(l)
            aux_lst = toList([tree], [])
            if aux_lst not in aux:
                r.append(tree)
                aux.append(aux_lst)
        
        # for aux in r:
        #     print(toList([aux], []))

        return r