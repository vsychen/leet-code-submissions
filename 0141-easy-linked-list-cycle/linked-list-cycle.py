# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # TOPICS: LINKED LIST/TWO POINTERS
    # If the list is empty or have only one element (does not have .next), return False. If the head is the same as the head.next, return True.
    # For anything else, add a second pointer. While the second pointer is not None and is different from the first pointer, advance the first pointer by
    # one position, and the second pointer by two positions. If there's no cycle, the second pointer will reach the end of the linked list first and
    # encounter None first; return False in this case. If there's a cycle, the second pointer will eventually reach the same node as the first
    # pointer, pointer1 == pointer2; return True in this case.
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head: return False
        elif not head.next: return False

        hare = head
        while hare and hare.next:
            head = head.next
            hare = hare.next.next

            if not hare: return False
            elif hare == head: return True
        return False
    
    # If the list is empty or have only one element (does not have .next), return False. If the head is the same as the head.next, return True.
    # For anything else, save the reference for the next node and update the next node to the current node. Use the saved reference to call the recursion.
    # If there's a cycle in the linked list, eventually it will come back to an already visited node. To identify an already visited node is simple, just
    # check if the .next is the same as the current node; return True if this happen. If there's no cycle, the .next pointer will eventually hit a None. 
    # In this case, return False.
    # def hasCycle(self, head):
    #     """
    #     :type head: ListNode
    #     :rtype: bool
    #     """
    #     if not head: return False
    #     elif not head.next: return False
    #     elif head == head.next: return True
    #     n = head.next
    #     head.next = head
    #     return self.hasCycle(n)