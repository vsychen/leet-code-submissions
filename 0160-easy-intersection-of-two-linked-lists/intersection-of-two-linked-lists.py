# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # TOPICS: LINKED LIST
    # If both heads have only one node, check if they are the same. Walk through both linked lists to get the number of nodes in each one. Get the size
    # difference between the two linked lists. If the difference is positive, walk the first list until the number of nodes is the same. If the difference
    # is negative, do the same with the second list. Now, both lists have the same number of nodes. Walk them both until a common node is found or until
    # the end of the lists. If a common node is found, that's the start of the intersection. If the end of the lists is found, there's no intersection.
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA.next and not headB.next: return headA if headA == headB else None
        curr = headA
        countA = 1
        while curr.next:
            curr = curr.next
            countA += 1
        curr = headB
        countB = 1
        while curr.next:
            curr = curr.next
            countB += 1
        
        diff = countA-countB
        if diff > 0:
            for i in range(diff):
                headA = headA.next
        elif diff < 0:
            for i in range(-diff):
                headB = headB.next
        
        while headA != headB and headA.next and headB.next:
            headA = headA.next
            headB = headB.next
        
        if headA == headB: return headA
        else: return None
