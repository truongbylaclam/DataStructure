# Linked List Template

# Node Module
class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = NULL
    def getVal(self):
        return self.val
    def setVal(self, val):
        self.val = val
    def getNext(self):
        return self.next
    def setNext(self, next):
        self.next = next

# Linked List Module
class LinkedList(object):
    def __init__(self, head= None):
        self.head = head
        self.count = 0


