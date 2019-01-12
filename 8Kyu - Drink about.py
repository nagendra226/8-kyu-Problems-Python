def people_with_age_drink(age):
    if(age<14):
        return 'drink toddy'
    elif(age>=14 and age<18):
        return 'drink coke'
    elif(age>=18 and age<21):
        return 'drink beer'
    else:
        return 'drink whisky'
