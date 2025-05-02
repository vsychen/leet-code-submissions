# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getSmaller(self, lists):
        smallerNode = None
        aux = 0
        for i in range(len(lists)):
            if lists[i] == [] or lists[i] == None: pass
            elif smallerNode == None or lists[i].val < smallerNode.val:
                smallerNode = lists[i]
                aux = i
        return (aux, smallerNode)

    def merge(self, lists): 
        if len(lists) == 0: return None

        (aux, node) = self.getSmaller(lists)
        if lists[aux].next == None: lists.pop(aux)
        else: lists[aux] = lists[aux].next
        
        node.next = self.merge(lists)
        return node

    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        lists = [l for l in lists if l != None]
        if len(lists) == 0: return None

        return self.merge(lists)