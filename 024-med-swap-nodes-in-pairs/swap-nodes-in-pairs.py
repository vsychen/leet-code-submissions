# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    # TOPICS: LINKED LIST/RECURSION
    # Base case, if list is empty, return empty list; if list has only one element, return said element.
    # The swap is done in pairs because our base case includes both cases node = None and node.next = None. If head = None, the list has even number of nodes, and 
    # all of them aready swapped. If head.next = None, the list has and odd number of nodes, and the last node does not need to swap. For the step cases, it is
    # enough to swap the node and node.next values and check for the node.next.next node.
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head == None: return None
        elif head.next == None: return head
        else: 
            temp = head.val
            head.val = head.next.val
            head.next.val = temp
            head.next.next = self.swapPairs(head.next.next)
        return head