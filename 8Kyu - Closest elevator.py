def elevator(left, right, call):
    if(abs(call -left) < abs(call-right)):
        return 'left'
    else:
        return 'right'
