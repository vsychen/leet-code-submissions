# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    # TOPICS: LINKED LIST/RECURSION
    # Check first element of each LinkedList. Select the smaller value node and set its next node to be the return of the recursive call. The base cases are
    # if both nodes are empty, the node is empty (None); (2) if the first list node is empty, the node is from the second list; alternatively, if the
    # second list is empty, the node comes from the first list. After setting the next nodes as the return from recursive calls, the list resulting from the merge 
    # will be sorted in an ascending order.
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