def say_hello(name, city, state):
    #your code here
    result_string = ""
    for val in name:
        result_string = result_string + ' ' + str(val)
    return 'Hello,{}! Welcome to {}, {}!'.format(result_string,city,state)
        
