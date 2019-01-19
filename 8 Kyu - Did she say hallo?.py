def validate_hello(greetings):
    #your code here
    if('hello' in greetings.lower()):
        return True
    elif('ciao' in greetings.lower()):
        return True
    elif('salut' in greetings.lower()):
        return True
    elif('hallo' in greetings.lower()):
        return True
    elif('hola' in greetings.lower()):
        return True
    elif('ahoj' in greetings.lower()):
        return True
    elif('czesc' in greetings.lower()):
        return True
    else:
        return False
  
    
