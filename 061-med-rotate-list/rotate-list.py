# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    # TOPICS: LINKED LIST
    # Base cases: Empty Linked List, return None as head; Linked List has one element, or k == 0 (no rotations), return head as head. Special case: number of rotations divided by number of
    # elements have rest equal to 0; return head as head (it will rotate and go back to the starting position).
    # First, if possible, reduce the number of rotations (if k>=l, the first l movements will bring the list to the starting position). When 1<=k<=l, calculate how many elements need to be
    # shifted (l-k). Save the reference to the head of the list and go to the (l-k-1)-th element, this element is the separation point. Set its next to None (it will be the last element of
    # the list). The next element will be the new first head. Then, go to the end of this sublist and point the end of the sublist to the previous first head.
    # ABCDE -> AB CDE -> CDE AB -> CDEAB
    def getLength(self, head):
        if head.next == None:
            return 1
        else:
            return 1+self.getLength(head.next)

    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head: return None
        elif not head.next or k == 0: return head
        else:
            l = self.getLength(head)
            if k >= l: k = k%l
            if k == 0: return head
            else:
                temp_head = head
                c = l-k
                while c > 1:
                    head = head.next
                    c -= 1

                aux = head.next
                head.next = None
                head = aux
                while aux.next:
                    aux = aux.next
                
                aux.next = temp_head
                return head