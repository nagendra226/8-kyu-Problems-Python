def bmi(weight, height):
    #your code here
    body_mass_index = weight/(height**2)
    
    if body_mass_index <= 18.5:
        return 'Underweight'
    elif body_mass_index <= 25.0:
        return 'Normal'
    elif body_mass_index <= 30.0:
        return 'Overweight'
    elif body_mass_index > 30:
        return 'Obese'
