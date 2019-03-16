import string
def lowercase_count(strng):
    # Your code here
    count = 0
    for i in strng:
        if i in string.ascii_lowercase:
            count = count + 1
    return count 
