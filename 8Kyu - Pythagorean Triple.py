def pythagorean_triple(integers):
    integers = tuple(integers)
    a,b,c = sorted(integers)
    if ((c**2) == (a**2 + b**2)):
        return bool(1)
    else:
        return bool(0)
    
