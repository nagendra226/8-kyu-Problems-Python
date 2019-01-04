def enough(cap, on, wait):
    # Your code here
    if (cap >= on + wait):
        return 0
    elif(on>wait and on>cap):
        on = on - cap
        return on + wait
    else:
        cap = cap - on
        return wait - cap
