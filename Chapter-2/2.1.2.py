# Solution 2.1.2

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

# size(self): gives the size of the list, or the number of elements in the list.
    def size(self):
        counter = 0
        current = self.head
        while current != None:
            counter += 1
            current = current.getNext()
        return counter
        
# add(self, item): adds an item to the start of the list.
    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

# remdup(self): removes duplicates from an unsorted linked list.
    def remdup(self):
        temp = []
        current = self.head
        previous = None
        while current != None:
            if previous == None:
                temp.append(current.getData())
                previous = current
                current = current.getNext()
            elif (current.getData() in temp) and (previous != None):    
                current = current.getNext()
            elif (current.getData() not in temp) and (previous != None):
                temp.append(current.getData())
                previous.setNext(current)
                previous = current
                current = current.getNext()
        if current == None:
            previous.setNext(current)

############################################
## Test
############################################

mylist = UnorderedList()
mylist.add(1)
mylist.add(2)
mylist.add(3)
mylist.add(4)
mylist.add(5)
mylist.add(1)
mylist.add(5)
mylist.add(23)
mylist.add(4)

print "Before deduplication:"
print "List size:", mylist.size()
print "Print elements in the list:"
mylist.prl()
print "After deduplication:"
mylist.remdup()
print "List size:", mylist.size()
print "Print elements in the list:"
mylist.prl()
