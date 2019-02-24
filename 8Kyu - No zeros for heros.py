def no_boring_zeros(n):
    # your code
    if n == 0:
        return 0
    else:
        n = str(n)
        return int(n.rstrip('0'))
