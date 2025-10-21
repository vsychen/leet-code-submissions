# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # TOPICS: LINKED LIST/TREE/BINARY TREE/BINARY SEARCH TREE/DIVIDE AND CONQUER
    # If the linked list's head is None, the tree's root is also empty. If there's only one node in the list, there's also one node in the tree. Walk through the Linked List, counting the
    # number of elements. Take the middle element, splitting the Linked List in two, and excluding the middle element. Create a tree where the middle element (pivot) is the root value and
    # the left subtree is a recursive call using the left Linked List, while the right subtree is the recursive call using the right Linked List.
    def split(self, head, mid):
        sec_head = head
        pivot = None
        while mid > 1:
            sec_head = sec_head.next
            mid -= 1
        
        pivot = sec_head.next
        sec_head.next = None
        sec_head = pivot.next

        return (head, pivot, sec_head)

    def sortedListToBST(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[TreeNode]
        """
        if not head: return None
        elif not head.next: return TreeNode(head.val)
        curr = head
        n = 0

        while curr:
            curr = curr.next
            n += 1

        mid = n >> 1

        (left, pivot, right) = self.split(head, mid)

        return TreeNode(pivot.val, self.sortedListToBST(left), self.sortedListToBST(right))