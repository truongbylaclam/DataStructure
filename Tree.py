import math
### Basic Tree ###
class Node:
    # Constructor
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
    # Mutator
    ## Insertion
    def insert(self,data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
            else:
                self.data = data
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()

# Implementaion
root = Node(10)
root.insert(6)
root.insert(14)
root.insert(3)
root.PrintTree()



def insertion(self,data):
    if self.data:
        if data < self.data:
            if self.left == None:
                self.left = Node(data)
            else:
                self.left.insertion(data)
        elif data < self.data:
            if self.right == None:
                self.right = Node(data)
            else:
                self.right.insertion(data)
        else:
            self.data = data