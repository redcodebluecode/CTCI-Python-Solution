# Capsule all the general classes and operations (methods) in one Module.

# Create a Node class
class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None
    
    def getData(self):
        return self.data
    
    def getNext(self):
        return self.next
    
    def setData(self, newdata):
        self.data = newdata
    
    def setNext(self, newnext):
        self.next = newnext
        
# Create an Unordered List class
class UnorderedList:
    def __init__(self):
        self.head = None

# Unorderd List Operations
# prl(self): prints out all the items in the list. Prints "Empty" if no elements in the list.
    def prl(self):
        if self.head == None:
            print "Empty"
        else:
            current = self.head
            while current != None:
                print current.getData()
                current = current.getNext()

# add(self, item): adds an item to the start of the list.
    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

# size(self): gives the size of the list, or the number of elements in the list.
    def size(self):
        counter = 0
        current = self.head
        while current != None:
            counter += 1
            current = current.getNext()
        return counter
