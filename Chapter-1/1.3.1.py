string1 = "ABCabc123!@#ABCabc123!@#"

string2 = "The quick brown fox jumps over the lazy dog.".lower() + "CHAPTER I. Down the Rabbit-Hole Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, 'and what is the use of a book,' thought Alice 'without pictures or conversations?'".lower()

# Method 1.3.1
def solution(s):
    newS = ""
    dictS = {}
    for i in range(len(s)):
        if s[i] not in dictS:
            newS += s[i]
            dictS[s[i]] = 1
    return newS
        
# test
print solution(string1)
print "Expected: ABCabc123!@#"
print solution(string2)
print "Expected: the quickbrownfxjmpsverlazydg.-,:'?"
