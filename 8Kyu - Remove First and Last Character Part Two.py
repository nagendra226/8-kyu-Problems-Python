def array(string):
    #your code here
    if len(string)<=4:
        return None
    else:
        return string[2:len(string)-2].replace(',',' ')
