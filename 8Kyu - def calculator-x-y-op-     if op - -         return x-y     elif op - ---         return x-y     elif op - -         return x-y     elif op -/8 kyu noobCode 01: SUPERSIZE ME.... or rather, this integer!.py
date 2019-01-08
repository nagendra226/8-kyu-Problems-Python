def super_size(n):
    #your code here
    string_number = str(n)
    sort_string = sorted(string_number,reverse = True)
    new_number = ''
    for number in sort_string:
        new_number += number
    return int(new_number)
