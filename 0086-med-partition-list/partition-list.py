# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    # TOPICS: LINKED LIST/TWO POINTERS
    # Create two nodes with value -1. Walk the original list looking for the value of each node; if it's less than x, add to the first created list as the next node; otherwise,
    # add to the second created list as the next node. When there's no more elements on the original list, clear any left "next"s on the second created list and make the end of
    # the first created list link to the start of the second created list.
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """
        if head == None: return None
        elif head.next == None: return head

        sp = ListNode(-1)
        less = sp
        ep = ListNode(-1)
        greater = ep

        while head:
            if head.val < x:
                sp.next = head
                sp = sp.next
            else:
                ep.next = head
                ep = ep.next
            head = head.next
        
        ep.next = None
        sp.next = greater.next

        return less.next