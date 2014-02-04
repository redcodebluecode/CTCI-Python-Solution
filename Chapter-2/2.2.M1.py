# Assume the elements are already in a python list (not a linked list).

# Solution 2.2.M1

def solution(mylist, pos):
    n = len(mylist)
    return mylist[n-pos]
    
# Test
l = [1,2,3,4]
print solution(l, 1)
print "Expected: 4"

print solution(l, 2)
print "Expected: 3"

print solution(l,4)
print "Expected: 1"
