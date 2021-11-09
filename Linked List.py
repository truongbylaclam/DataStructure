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
    def getCount(self):
        return self.count;
    def insert(self, data):
        new_node = Node(data)
        new_node.setNext(self.head)
        self.head = new_node
        self.count += 1;
    def find(self, val):
        item = self.head
        while (item != None):
            if item.getVal() == val:
                return item
            else:
                item = item.getNext()


Item = LinkedList()
Item.insert(10)
Item.insert(20)
Item.insert(30)

print("Item count", Item.getCount())
print("Finding Item", Item.find(20))