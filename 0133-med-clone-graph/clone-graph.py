"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    # TOPICS: GRAPH/BFS
    # If root node is empty, return None. If there's only one node, return a new node with the same value. For any graph with more than one node, use BFS
    # to walk through it, creating a copy of the old nodes with the same value and neighbors. The question restricts the node's value to a index, and all 
    # nodes need to be reachable; make a list of nodes to keep them organized and every time a node with value bigger than the size of the list, add new
    # nodes to the list until the quantity of nodes is the same as the biggest value. At the end of the loop, all nodes need to have a list of neighbors
    # and the nodes will be sorted by value. Return the very first one as the answer.
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node: return None
        elif not node.neighbors: return Node(node.val, None)

        toCheck = [node]
        lst = []

        while toCheck:
            curr = toCheck.pop(0)

            while len(lst) < curr.val:
                lst.append(Node(len(lst)+1, None))

            if lst[curr.val-1].neighbors == []:
                max_nodes = max([n.val for n in curr.neighbors])
                while len(lst) < max_nodes: lst.append(Node(len(lst)+1, None))
                lst[curr.val-1].neighbors = [lst[n.val-1] for n in curr.neighbors]
                toCheck.extend(curr.neighbors)

        return lst[0]