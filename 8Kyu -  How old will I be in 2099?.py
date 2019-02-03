def calculate_age(year_of_birth, current_year):
    #your code here
    age = current_year - year_of_birth
    if(year_of_birth>current_year and age == -1):
        return 'You will be born in {} year.'.format(abs(age))
    elif(year_of_birth<current_year and age == 1):
        return 'You are {} year old.'.format(age)
        
    if(age<0):
        return 'You will be born in {} years.'.format(abs(age))
    elif(age>0):
        return 'You are {} years old.'.format(age)
    else:
        return 'You were born this very year!'
