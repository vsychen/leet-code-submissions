"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    # TOPICS: LINKED LIST
    # If empty list, return empty list. First, walk through the original linked list and save it into a list, adding a new index information on each node. 
    # Create a new list of nodes from scratch with dummy values. Walk through the new nodes updating their values, the reference to the next and to the 
    # random nodes, using the index info to accurately determine the position of the random node inside the lists. At the end of the iteration, return the
    # first element of the new list as the head of the new linked list.
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head: return None
        old_nodes = []

        while head:
            head.index = len(old_nodes)
            old_nodes.append(head)
            head = head.next
        
        new_nodes = [Node(0) for _ in range(len(old_nodes))]
        for i in range(len(new_nodes)):
            new_nodes[i].val = old_nodes[i].val
            new_nodes[i].next = new_nodes[i+1] if i+1 < len(new_nodes) else None
            new_nodes[i].random = new_nodes[old_nodes[i].random.index] if old_nodes[i].random else None

        return new_nodes[0]