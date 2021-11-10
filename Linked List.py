# Linked List Template

# Node Module
class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None
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
<<<<<<< HEAD
        self.count = 0  
    def getCount(self):
        return self.count
=======
        self.count = 0
    def getCount(self):
        return self.count;
>>>>>>> 769cc19d5d48b1bdf476c6cf414e4ac603cb944e
    def insert(self, data):
        new_node = Node(data)
        new_node.setNext(self.head)
        self.head = new_node
<<<<<<< HEAD
        self.count += 1
        print("Insert completed")
    def find(self, val):
        item = self.head
        while (item != None):
            if (item.getVal() == val):
                return item
            else:
                item = item.getNext()
        return None
    def deleteAt(self, idx):
        if idx > self.count - 1:
            return
        if idx == 0:
            self.head = self.head.getNext();
        else:
            tempidx = 0
            return
=======
        self.count += 1;
    def find(self, val):
        item = self.head
        while (item != None):
            if item.getVal() == val:
                return item
            else:
                item = item.getNext()
>>>>>>> 769cc19d5d48b1bdf476c6cf414e4ac603cb944e

list = LinkedList()
list.insert(10)

print(list.getCount())

Item = LinkedList()
Item.insert(10)
Item.insert(20)
Item.insert(30)

print("Item count", Item.getCount())
print("Finding Item", Item.find(20))