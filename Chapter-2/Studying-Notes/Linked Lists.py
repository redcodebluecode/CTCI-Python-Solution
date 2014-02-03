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
print "Create a new Node and get its data:"
testnode = Node(17)
print testnode.getData()

##########################################
## Step 2: Create an Unordered List class
##########################################

class UnorderedList:

    def __init__(self):
        self.head = None

###########################################
## Step 3: Create List operations
###########################################

# isEmpty()
    def isEmpty(self):
        return self.head == None

    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self,item):
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

#################################
## Test
#################################
print "Test Step 2:"
print "Create a new unorderedlist:"
mylist = UnorderedList()

print "Test Step 3:"
print "Test whether the list is empty:", mylist.isEmpty()

print "Add items to the list:"
mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)

print "Test whether the list is empty:", mylist.isEmpty()

print(mylist.size())
print(mylist.search(93))
print(mylist.search(100))

mylist.add(100)
print(mylist.search(100))
print(mylist.size())

mylist.remove(54)
print(mylist.size())
mylist.remove(93)
print(mylist.size())
mylist.remove(31)
print(mylist.size())
print(mylist.search(93))
        
