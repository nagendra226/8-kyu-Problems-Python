def array_madness(a,b):
    # Ready, get, set, GO!!!
    sum_a = 0
    sum_b = 0
    for num in a:
        sum_a = sum_a + num**2
    for num in b:
        sum_b = sum_b + num**3
    return sum_a>sum_b
