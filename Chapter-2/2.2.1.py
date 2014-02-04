# Solution 2.2.1

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

# Build Unordered List operations

# add(): adds an element to the start of the list.
    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

# size(): returns the number of elements in the list.
    def size(self):
        counter = 0
        current = self.head
        while current != None:
            counter += 1
            current = current.getNext()
        return counter

# prl(): prints out the elements in the list.
    def prl(self):
        current = self.head
        while current != None:
            print current.getData()
            current = current.getNext()
            
# lastnth(): finds the nth element  to last element of a singly linked list, and returns it.
    def lastnth(self, k):
        current = self.head
        previous = None
        counter = 0
        while counter < k:
        
        TBD
            
