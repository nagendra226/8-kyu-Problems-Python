def is_lock_ness_monster(string):
    #your code here
    if string.find('tree fiddy')>0:
        return True
    elif string.find('3.50')>0:
        return True
    elif string.find('three fifty')>0:
        return True
    else:
        return False
