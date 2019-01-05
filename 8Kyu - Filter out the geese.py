geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
def goose_filter(birds):
    #your code here
    new = []
    for i in birds:
        if i not in geese:
            new.append(i)
    return new
