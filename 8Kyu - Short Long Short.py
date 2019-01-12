def solution(a, b):
    pass
    m = len(a)
    n = len(b)
    if(m>n):
        return '{}{}{}'.format(b,a,b)
    else:
        return '{}{}{}'.format(a,b,a)
