"""
The Unordered List Abstract Data Type
The structure of an unordered list is a collection of items where each item holds a relative position with respect to the others. Some possible unordered list operations are given below.

List() creates a new list that is empty. It needs no parameters and returns an empty list.

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

# insert

# index

# pop
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

print "Test whether the list is empty:", mylist.isEmpty()

print "Returns the number of items in the list", mylist.size()

print "Search whether an item is in the list:"
print(mylist.search(99))
print(mylist.search(18))

print "Remove an item:"
print(mylist.size())
mylist.remove(16)
print(mylist.size())
mylist.remove(99)
print(mylist.size())
mylist.remove(35)
print(mylist.size())
print(mylist.search(99))

print "Append an item to a non-empty list:"
print mylist.isEmpty()
print mylist.size()
mylist.append(100)
print mylist.size()

print "Append an item to an empty list:"
mylist2 = UnorderedList()
print mylist2.isEmpty()
print mylist2.size()
mylist2.append(101)
print mylist2.isEmpty()
print mylist2.size()
