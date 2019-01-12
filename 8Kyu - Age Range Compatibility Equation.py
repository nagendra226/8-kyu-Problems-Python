def dating_range(age):
    #return min-max
    if(age<=14):
        min_age = int(age - (0.10*age))
        max_age = int(age + (0.10*age))
    
    else:
        min_age = int((age/2) + 7)
        max_age = int((age-7)*2)
    return "{}-{}".format(min_age,max_age)
