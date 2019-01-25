def parse_float(string):
    pass
    string = ''.join(string)
    try:
        if(string.isalnum()):
            return None
        else:
            return float(string)
    except:
        return None
