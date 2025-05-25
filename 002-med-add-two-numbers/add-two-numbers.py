# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    # TOPICS: LINKED LIST/RECURSION/MATH
    # Just sum the values of the nodes of the two Linked Lists. If there's a carry on, it is necessary to add it to the next sum.
    def addTwoNumbers2(self, l1, l2, carry):
        n1 = 0 if not l1 else l1.val
        n2 = 0 if not l2 else l2.val

        val = n1+n2+carry
        carry = 1 if val >= 10 else 0
        val = val%10

        if not l1 and not l2:
            return ListNode(val = val, next = None) if val > 0 else None
        else:
            a = None if not l1 else l1.next
            b = None if not l2 else l2.next
            return ListNode(val = val, next = self.addTwoNumbers2(a, b, carry))

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        return self.addTwoNumbers2(l1, l2, 0)
        
