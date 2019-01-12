import math
def calculate_tip(amount, rating):
    #your code here
    if(rating.lower() == 'poor'):
        return math.ceil(amount*0.05)
    elif(rating.lower() == 'terrible'):
        return 0
    elif(rating.lower() == 'good'):
        return math.ceil(amount*0.1)
    elif(rating.lower() == 'great'):
        return math.ceil(amount*0.15)
    elif(rating.lower() == 'excellent'):
        return math.ceil(amount*0.2)
    else:
        return 'Rating not recognised'
    
        
 Correct! You may take your time to refactor/commen
