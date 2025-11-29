class ListNode(object):
    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache(object):
    # TOPICS: LINKED LIST/HASH TABLE
    # Cache where, when full, it deletes the least recently used entry before adding new data.
    # For the design of this cache, both a double linked list and a dictionary were used. The node of the linked list contains the attributes key, value
    # prev and next while the dictionary has the key as key and the full node as value. The key value appears both inside the node and as key in the
    # dictionary to help optimize the removal of a node, when necessary.

    # self.capacity -> cache storage limit
    # self.head     -> linked list head node
    # self.tail     -> linked list tail node
    # self.values   -> key/value dict
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.head = self.tail = None
        self.values = {}
    
    # Move a node to the start of the linked list. If the list has only one element, do nothing. If the node to be moved is already the head of the list,
    # do nothing. If the node is the tail, change the .tail reference to the previous node; otherwise, isolate the node, removing the current node from the
    # reference of the previous/next nodes. Finally, set the references of the current node and the .head node to each other and update the .head to the
    # current node.
    def moveNode(self, node):
        if len(self.values) >= 2:
            if node == self.head: pass # If node is head, don't need to do anything
            else:
                if node == self.tail: # If node is tail, need to change tail reference
                    self.tail = node.prev
                    self.tail.next = None
                else:
                    prev_ = node.prev
                    next_ = node.next
                    if prev_: prev_.next = next_
                    if next_: next_.prev = prev_
                
                node.prev = None
                node.next = self.head
                self.head.prev = node
                self.head = node

    # Get the value attibuted to a key. If the key is not in the dictionary, return -1. Otherwise, return the value of the node to the user. The node also
    # needs to be moved up to the start of the linked list, if found.
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.values.keys(): return -1

        node = self.values[key]
        self.moveNode(node)
        return node.val

    # Put a pair key/value into the cache. If the key already exists in the dictionary, update its value. Otherwise, make a new node. If the dictionary
    # is empty or is full with with capacity=1, remove the old value from the dictionary if any exists, and then add the new node as both .head and .tail.
    # For any other case, first remove the .tail node if the cache's capacity is full (remember to remove from both dictionary and linked list) and update 
    # the references of the .head and the current node and update the new .head to the current node. Add the pair key/value to the dictionary too. If 
    # necessary, move the node to the head position too.
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        node = None
        if key in self.values.keys():
            node = self.values[key]
            node.val = value
        else:
            node = ListNode(key, value)
            if len(self.values) == 0 or (len(self.values) == 1 and len(self.values) == self.capacity):
                if len(self.values) == self.capacity: self.values.pop(self.head.key) # Remove LRU
                self.head = self.tail = node
            else:
                if len(self.values) == self.capacity: # Remove LRU
                    tail_ = self.values.pop(self.tail.key)
                    self.tail = tail_.prev
                    self.tail.next = None

                self.head.prev = node
                node.next = self.head
                self.head = node

            self.values[key] = node

        self.moveNode(node)
        return