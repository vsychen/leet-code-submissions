# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
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