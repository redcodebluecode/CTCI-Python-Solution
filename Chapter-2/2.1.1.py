# Solution 2.1.1
# There is bug to be fixed. Remove the hash tags in the test part, and you will see the bugs.
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
        
# remdup(self): removes duplicates from an unsorted linked list.
    def remdup(self):
        # Your code here:
        current = self.head
        previous = self.head
        while previous.getNext() != None:
            while current.getNext() != None:
                current = current.getNext()
                if previous.getData() == current.getData():
                    previous.setNext(current.getNext())
                else:
                    pass
            previous = previous.getNext()
            current = previous.getNext()

############################################
## Test
############################################

mylist = UnorderedList()
mylist.add(1)
# mylist.add(1)
mylist.add(2)
# mylist.add(2)
mylist.add(3)
# mylist.add(3)
mylist.add(4)
mylist.add(2)
mylist.add(3)
mylist.add(4)
mylist.add(3)
mylist.add(4)
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
