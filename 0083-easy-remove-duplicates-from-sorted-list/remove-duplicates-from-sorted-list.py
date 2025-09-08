# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    # TOPICS: LINKED LIST
    # If there's no head, return None. If there's only the head, return it. For anything with two or more nodes:
    # If the next node is empty, check if the value of the current node is equal to the value being passed; if it is, return None; it it isn't, return the node.
    # If the next node isn't empty, check if the value of the current node is equal to the value being passed; if it is, return the call to the method passing the 
    # next node and the current value as the current node. If it isn't, point the call to the method passing the next node and the current value as the next node 
    # to the current node and return the current node back to the previous call to update the node list.
    def doIt(self, head, val):
        if head.next == None:
            if head.val == val: return None
            else: return head
        else:
            if head.val == val: return self.doIt(head.next, head.val)
            else:
                head.next = self.doIt(head.next, head.val)
                return head

    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head == None: return None
        elif head.next == None: return head
        return self.doIt(head, -101)