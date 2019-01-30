def find_longest(string):
    spl = string.split(" ")
    longest = 0
    for x,i in enumerate(spl):
        if (len(spl[x]) > longest): 
            longest = len(spl[x])
    return longest
