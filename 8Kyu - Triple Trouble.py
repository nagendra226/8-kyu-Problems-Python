def triple_trouble(one, two, three):
    #your code here
    list1 = [i for i in one]
    list2 = [i for i in two]
    list3 = [i for i in three]
    result_string = ""
    for (x,y,z) in zip(list1,list2,list3):
        result_string = result_string+x+y+z
    return result_string
