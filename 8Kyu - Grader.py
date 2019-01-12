def grader(score):
    if(score<0.6 or score>1):
        return 'F'
    elif(score==0.6):
        return 'D'
    elif(score>=0.9):
        return 'A'
    elif(score==0.7):
        return 'C'
    elif(score==0.8):
        return 'B'
