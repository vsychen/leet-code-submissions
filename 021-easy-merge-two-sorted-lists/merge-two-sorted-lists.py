# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def merge(self, l1, l2):
        if l1 == None and l2 == None: return None
        elif l1 == None: return l2
        elif l2 == None: return l1
        elif l1.val < l2.val:
            l1.next = self.merge(l1.next, l2)
            return l1
        elif l1.val >= l2.val:
            l2.next = self.merge(l1, l2.next)
            return l2

    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        return self.merge(list1, list2)