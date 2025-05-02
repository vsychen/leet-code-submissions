# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNth(self, node, to_remove, pos):
        if to_remove == pos:
            return node.next
        else: 
            node.next = self.removeNth(node.next, to_remove, pos+1)
            return node

    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        size = 1
        temp = head

        while temp.next:
            temp = temp.next
            size += 1

        head = self.removeNth(head, size-n, 0)

        return head