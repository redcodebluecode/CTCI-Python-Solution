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
            
# lastnth(): finds the nth element to last element of a singly linked list, and returns it.
    def lastnth(self, k):
        index = self.head
        current = index
        while current.getNext() != None:
            counter = k
            current = index
            while counter != 0:
                current = current.getNext()
                counter -= 1
            if current.getNext() == None:
                return index.getNext().getData()
            else:
                index = index.getNext()
            #print index.getData(), current.getData()
            
############################################
## Test
############################################

mylist = UnorderedList()
mylist.add(1)

mylist.add(2)
mylist.add(3)
mylist.add(4)
mylist.add(5)

print "List size:", mylist.size()
print "Print elements in the list:"
mylist.prl()
print mylist.lastnth(1)

print mylist.lastnth(2)
"""
print mylist.lastnth(3)
print mylist.lastnth(4)
"""
print mylist.lastnth(5)

