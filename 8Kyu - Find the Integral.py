def integrate(coefficient, exponent):
    # write your code here
    y = float((((coefficient) / (exponent + 1))))
    if y.is_integer():
        y = str(y)
        y =  y.replace('.0','')
    else:
        y = str(y)
    return y+'x'+'^'+str(exponent+1)
