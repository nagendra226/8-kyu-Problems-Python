def index(array, n):
    length_array = len(array)
    if n>length_array-1:
        return -1
    else:
        return array[n]**n
