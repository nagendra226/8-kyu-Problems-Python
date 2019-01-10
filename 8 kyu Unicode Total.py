def uni_total(string):
    #your code here
    total = 0
    for i in string:
        total = total + ord(i)
    return total
