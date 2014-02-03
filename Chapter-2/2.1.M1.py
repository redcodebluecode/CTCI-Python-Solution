# Assume the elements are already in a python list (not a linked list). Here are the ways to do the de-duplication.

# Solution 2.1.M1.1
def dedup1(mylist):
    newlist = list(set(mylist))
    print newlist

# Solution 2.1.M1.2
def dedup2(mylist):
    temp = dict.fromkeys(mylist)
    newlist = temp.keys()
    print newlist

# Solution 2.1.M1.3
def dedup3(mylist):
    newlist = []
    for element in mylist:
        if element not in newlist:
            newlist.append(element)

# Test
testlist = [2, 4, 1, 3, 2, 3, 4, 5, 3]

dedup1(testlist)
print "Expected: [1,2,3,4,5]"
dedup2(testlist)
print "Expected: [1,2,3,4,5]"
dedup3(testlist)
print "Expected: [1,2,3,4,5]"
