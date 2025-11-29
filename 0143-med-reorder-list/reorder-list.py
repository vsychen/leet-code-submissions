# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    # TOPICS: LINKED LIST
    # Start a list/queue and put all nodes inside it. While this list has more than two elements, pick the last one and insert it between the first two, and then
    # remove both the first and last elements of the list/queue.
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        nodes = []
        curr = head

        while curr:
            nodes.append(curr)
            curr = curr.next
        
        while nodes:
            if len(nodes) <= 2: nodes.pop()
            else:
                nodes[-2].next = None
                nodes[0].next = nodes[-1]
                nodes[-1].next = nodes[1]
                nodes.pop()
                nodes.pop(0)