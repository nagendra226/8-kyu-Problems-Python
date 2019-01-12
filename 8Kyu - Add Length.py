def add_length(str_):
    #your code here
    li = []
    x = ''
    for i in str_.split():
        x = '{} {}'.format(i,len(i))
        li.append(x)
    return li
