def square_or_square_root(arr):
    new_li = []
    for i in arr:
        x = i**0.5
        if(x.is_integer()):
            new_li.append(x)
        else:
            new_li.append(i**2)
    return new_li
            
