# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

class Solution(object):
    # TOPICS: LINKED LIST/TWO POINTERS
    # If empty list or list has only one element and not .next, return None. Walk through the linked list with two pointers, one walking one node a time, the other
    # walking two nodes at a time. If the fast pointer finds the end of the list, return None. Otherwise, they will eventually meet at some point of the existing
    # loop. When they meet, reset the slow pointer to the head of the linked list again. Walk through the linked list on both pointers, one node at a time for both.
    # The next time they meet will be the loop starting point.
    # Mathematical explanation: Consider a linked list starting on n1, loop starting at n2, and n3 being the first point where the two pointers meet.
    # While the slow pointer will traverse s1 (n1->n2) plus s2 (n2->n3), the fast pointer will traverse s1, s2 and then start looping s3 and s2 again.
    # The formula would be something like 2*(s1+s2)=s1+s2+x*(s3+s2), where x can be considered 1 (it does not matter how many times the fastest pointer loop, it will
    # end up in the same 'meet point'). So, 2*(s1+s2)=s1+s2+s3+s2. After solving the equation, s1=s3, which means the time/quantity of nodes needed to go from start
    # to the cycle starting point is the same time/quantity of nodes needed to go from the meeting point to the cycle starting point. After the two pointers meet
    # for the first time, the slow pointer is reset to the start of the list, and the fast pointer start counting from the meeting point. Walking at the same pace,
    # they will eventually meet at the cycle starting point.
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return None
        elif not head.next: return None

        tort = hare = head
        while hare and hare.next:
            tort = tort.next
            hare = hare.next.next

            if not hare or not hare.next: return None
            elif hare == tort: break
        
        tort = head
        while tort != hare:
            tort = tort.next
            hare = hare.next

        return hare