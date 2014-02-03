"""
The Unordered List Abstract Data Type
Source: http://interactivepython.org/courselib/static/pythonds/BasicDS/linkedlists.html

The structure of an unordered list is a collection of items where each item holds a relative position with respect to the others. Some possible unordered list operations are given below.

List() creates a new list that is empty. It needs no parameters and returns an empty list.

prl() print all the items in the list. It needs no parameters and prints all the items in the list. If the list is empty, it will print "Empty".

add(item) adds a new item to the list. It needs the item and returns nothing. Assume the item is not already in the list.

remove(item) removes the item from the list. It needs the item and modifies the list. Assume the item is present in the list.

search(item) searches for the item in the list. It needs the item and returns a boolean value.

isEmpty() tests to see whether the list is empty. It needs no parameters and returns a boolean value.

size() returns the number of items in the list. It needs no parameters and returns an integer.

append(item) adds a new item to the end of the list making it the last item in the collection. It needs the item and returns nothing. Assume the item is not already in the list.

index(item) returns the position of item in the list. It needs the item and returns the index. Assume the item is in the list.

insert(pos,item) adds a new item to the list at position pos. It needs the item and returns nothing. Assume the item is not already in the list and there are enough existing items to have position pos.

pop() removes and returns the last item in the list. It needs nothing and returns an item. Assume the list has at least one item.

pop(pos) removes and returns the item at position pos. It needs the position and returns the item. Assume the item is in the list.
"""

##################################
## Step 1: Create a Node class
##################################

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

print "Test Step 1:"
testnode = Node(17)
print "Create a new Node and get its data:", 
print testnode.getData()
print ""

##########################################
## Step 2: Create an Unordered List class
##########################################

class UnorderedList:

    def __init__(self):
        self.head = None

###########################################
## Step 3: Create List operations
###########################################

# prl(self): print all the items in the list
    def prl(self):
        if self.head == None:
            print "Empty"
        else:
            current = self.head
            while current != None:
                print current.getData()
                current = current.getNext()

# isEmpty(): tests to see whether the list is empty. It needs no parameters and returns a boolean value.
    def isEmpty(self):
        return self.head == None

# add(item): adds a new item to the list. It needs the item and returns nothing. Assume the item is not already in the list.
    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

# size(): returns the number of items in the list. It needs no parameters and returns an integer.
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count

# search(self, item): searches for the item in the list. It needs the item and returns a boolean value.
    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

# remove(self, item): removes the item from the list. It needs the item and modifies the list. Assume the item is present in the list.
    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
            
# append(item): adds a new item to the end of the list making it the last item in the collection. It needs the item and returns nothing. Assume the item is not already in the list.
    def append(self, item):
        current = self.head
        found = False
        temp = Node(item)
        while not found:
            if self.head == None:
                found = True
                self.head = temp
            elif (self.head != None) & (current.getNext() == None):
                found = True
                current.setNext(temp)
            else:
                current = current.getNext()

# insert(pos,item): adds a new item to the list at position pos. It needs the item and returns nothing. Assume the item is not already in the list and there are enough existing items to have position pos.
    def insert(self, item, pos):
        ind = 0
        temp = Node(item)
        previous = None
        current = self.head
        if pos == 0:
            temp.setNext(self.head)
            self.head = temp
        else:
            while ind < pos:
                ind += 1
                previous = current
                current = current.getNext()
            temp.setNext(current)
            previous.setNext(temp)
       
# index(self, item): returns the position of item in the list. It needs the item and returns the index. Assume the item is in the list.
    def index(self, item):
        ind = 0
        current = self.head
        found = False
        while not found:
            if current.getData() == item:
                found = True
                return ind
            else:
                current = current.getNext()
                ind += 1

# pop(self): removes and returns the last item in the list. It needs nothing and returns an item. Assume the list has at least one item.
    def pop(self):
        current = self.head
        previous = None
        if current.getNext() == None:
            self.head = None
        else:
            while current.getNext() != None:
                previous = current
                current = current.getNext()
            previous.setNext(None)
        return current.getData()
        
# poppos(self, pos): removes and returns the item at position pos. It needs the position and returns the item. Assume the item is in the list.
    def poppos(self, pos):
        ind = 0
        current = self.head
        previous = None
        if pos == 0:
            self.head = current.getNext()
        else:
            while ind < pos:
                ind += 1
                previous = current
                current = current.getNext()
            previous.setNext(current.getNext())
        return current.getData()
        
#################################
## Test
#################################

print "Test Step 2:"
print "Create a new unorderedlist:"
mylist = UnorderedList()
print ""

print "Test Step 3:"
print "Test whether the list is empty:", mylist.isEmpty()

print "Add items to the list:"
mylist.add(16)
mylist.add(26)
mylist.add(35)
mylist.add(99)
mylist.add(12)
mylist.add(49)
mylist.prl()

print "Test whether the list is empty:", mylist.isEmpty()

print "Returns the number of items in the list", mylist.size()

print "Search whether an item is in the list:"
print(mylist.search(99))
print(mylist.search(18))

print "Remove an item:"
print(mylist.size())
mylist.prl()
mylist.remove(99)
print(mylist.search(99))
print(mylist.size())
mylist.prl()

print "Append an item to a non-empty list:"
print mylist.isEmpty()
mylist.prl()
mylist.append(100)
print mylist.size()
mylist.prl()

print "Append an item to an empty list:"
mylist2 = UnorderedList()
print mylist2.isEmpty()
mylist.prl()
mylist2.append(101)
print mylist2.isEmpty()
mylist.prl()

print "Insert an item at a designated position:"
print "Before insertion:"
mylist.prl()
mylist.insert(0, 0)
mylist.insert(1, 1)
print "After insertion:"
mylist.prl()

print "Find the index of an item in the list:"
print mylist.index(0)
print mylist.index(1)
print mylist.index(100)

print "Pop the last item in the list:"
mylist.prl()
mylist.pop()
mylist.prl()

print "Pop an item at a designated position:"
mylist.prl()
mylist.poppos(0)
mylist.poppos(1)
mylist.prl()
