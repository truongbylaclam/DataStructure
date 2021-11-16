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
        self.count = 0  

    def get_count(self):
        return self.count

    def insert(self, data):
        new_node = Node(data)
        new_node.setNext(self.head)
        self.head = new_node
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
        if idx > self.count:
            return
        if idx == 0:
            self.head = self.head.getNext()
        else:
            tempidx = 0
            node = self.head
            while tempidx < idx - 1:
                node = node.getNext()
                tempidx += 1
            tempnode = self.head.getNext()
            node.setNext(tempnode.getNext())
            self.count -= 1
    def dump_list(self):
        tempnode = self.head
        while (tempnode != None):
            print("Node :", tempnode.getVal())
            tempnode = tempnode.getNext()


itemlist = LinkedList()
itemlist.insert(38)
itemlist.insert(49)
itemlist.insert(13)
itemlist.insert(15)

itemlist.dump_list()

# exercise the list
print("Item count: ", itemlist.get_count())
print("Finding item: ", itemlist.find(13))
print("Finding item: ", itemlist.find(78))

# delete an item
itemlist.deleteAt(3)
print("Item count: ", itemlist.get_count())
print("Finding item: ", itemlist.find(38))
itemlist.dump_list()


