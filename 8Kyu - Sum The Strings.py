def sum_str(a, b):
    # happy coding !
    if a == "" and b == "":
        return '0'
    elif  b is "" or b is " ":
        b = "0"
    elif a is "" or a == " ":
        a = "0"
    return str(int(a) + int(b))
