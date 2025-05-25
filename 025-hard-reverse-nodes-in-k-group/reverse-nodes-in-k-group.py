# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    # TOPICS: LINKED LIST/RECURSION
    # First check if the list has k nodes. If no, just return the list (it is not necessary to reverse them, as they do not have k nodes).
    # If there is k nodes, put all of these nodes in a list and, while visiting them in reverse (by list), change their node.next to the previous node (instead of next).
    # Repeat this operation for the next batch of k nodes and set the node.next of the previous first node (current last node) to the return of this recursive call.
    # Return the previous last node (currently first node). 
    def checkIfHasKNodes(self, head, k):
        for _ in range(k):
            if head == None: return False
            head = head.next
        return True

    def reverseKNodes(self, head, k):
        nodes = []
        for _ in range(k):
            nodes.append(head)
            head = head.next

        temp = nodes[k-1].next
        for i in range(len(nodes)-1, 0, -1):
            nodes[i].next = nodes[i-1]
        nodes[0].next = self.reverseKGroup(temp, k)
        return nodes[k-1]

    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if self.checkIfHasKNodes(head, k):
            head = self.reverseKNodes(head, k)
        
        return head