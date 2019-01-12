def get_number_from_string(string):
    val = ''
    for i in string:
        if i.isdigit():
            val = val + i
    return int(val)
