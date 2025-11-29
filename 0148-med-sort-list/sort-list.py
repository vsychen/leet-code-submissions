# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    # TOPICS: LINKED LIST/SORTING/TWO POINTERS/DIVIDE AND CONQUER
    # First get the size of the linked list. Then, start dividing the linked list in half and sorting each half separately. The result will be two sorted lists,
    # each with size n/2 or (n/2)+1 where n is the size of the original list. Walk through both lists picking the first element of lesser value until one of the lists is
    # empty. Finally, connect the rest of the non-empty list with the sorted nodes and return the head of the new sorted list.
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        size = 0
        curr = head
        while curr:
            size += 1
            curr = curr.next
        
        def mergeSort(ll, mid):
            if not ll: return
            elif not ll.next: return ll

            left = right = ll
            for i in range(mid):
                if i == mid-1:
                    aux = right
                    right = right.next
                    aux.next = None
                else:
                    right = right.next
            
            mid = mid >> 1
            if mid == 0: mid = 1
            left = mergeSort(left, mid)
            right = mergeSort(right, mid)
            head = aux = ListNode(-1)
            while left and right:
                if left.val < right.val:
                    aux.next = left
                    left = left.next
                else:
                    aux.next = right
                    right = right.next
                aux = aux.next

                if not left and right:
                    aux.next = right
                    break
                elif left and not right:
                    aux.next = left
                    break

            return head.next

        return mergeSort(head, size>>1)