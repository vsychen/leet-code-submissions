# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    # TOPICS: LINKED LIST
    # If left and right are the same, the list don't need to change, return the same list. Put a dummy head at the start of the list. Walk the list until the node before the ones
    # that will be reversed, it will be the temp1 node. the next node, i.e., the first node to be reversed will be temp2. the next node, i.e., the second node to be reversed will 
    # be temp3. temp3 is the only node that will be updated each iteration.
    # First, set temp3 as the node following temp2    HEAD -> N1 -> (temp1) N2 -> (temp2) N3 -> (temp3) N4 -> N5
    # Update temp2.next with temp3.next               HEAD -> N1 -> (temp1) N2 -> (temp2) N3 -> N5 // (temp3) N4 -> N5
    # Update temp3.next with temp1.next               HEAD -> N1 -> (temp1) N2 -> (temp2) N3 -> N5 // (temp3) N4 -> (temp2) N3 -> N5
    # Update temp1.next with temp3                    HEAD -> N1 -> (temp1) N2 -> (temp3) N4 -> (temp2) N3 -> N5
    # Repeat these steps (right-left) times.
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        if left == right: return head
        m = right - left

        aux = ListNode(-1, head)
        head = aux

        temp1 = head
        while left > 1:
            temp1 = temp1.next
            left -= 1
        
        temp2 = temp1.next
        while m > 0:
            temp3 = temp2.next
            temp2.next = temp3.next
            temp3.next = temp1.next
            temp1.next = temp3

            m -= 1
        return head.next