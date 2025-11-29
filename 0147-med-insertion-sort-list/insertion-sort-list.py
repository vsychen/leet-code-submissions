# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    # TOPICS: LINKED LIST/SORTING
    # If input has only one node, return it as the list. Create a new empty linked list. While the old linked list has nodes, split the .head node from the old
    # linked list and simulate an insertion. Walk through the list until the inserted node's value is less than the list's node's value. It's necessary to do 
    # an update of the .head node for each call, because it's possible the head will change with the sorting. When the old linked list is empty, return the head
    # of the new linked list.
    def insertionSortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head: return None
        elif not head.next: return head

        def insertSort(ll, node):
            if not ll:
                return node
            else:
                if ll.val < node.val:
                    ll.next = insertSort(ll.next, node)
                    return ll
                else:
                    node.next = ll
                    return node

        new_head = None
        while head:
            aux = head
            head = head.next
            aux.next = None
            new_head = insertSort(new_head, aux)
        
        return new_head