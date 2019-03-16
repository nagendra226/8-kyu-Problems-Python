def two_highest(arg1):
    pass
    if(type(arg1)==str):
        return False
    s = set(arg1)
    li = []
    s = list(s)
    s.sort()
    if(isinstance(s,(int,list))):
        try:
            if(len(s)==1):
                return li
            else:
                a=s[-1]
                b=s[-2]
                li.append(a)
                li.append(b)
                return li
        except:
            return li
    else:
        return False
        
