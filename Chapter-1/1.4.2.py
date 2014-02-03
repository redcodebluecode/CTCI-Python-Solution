string1 = "secure"
string2 = "rescue"

string3 = "I love apples."
string4 = "I love apples."

string5 = "I love iphones."

# Solution 1.4.2
def solution(s1, s2):
    l1 = sorted(s1)
    l2 = sorted(s2)
    if l1 == l2:
        return True
    else:
        return False

# test
print solution(string1, string2)
print "Expected: True"
print solution(string3, string4)
print "Expected: True"
print solution(string3, string5)
print "Expected: False"
