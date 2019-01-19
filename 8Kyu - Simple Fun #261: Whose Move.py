def whoseMove(lastPlayer, win):
    # Your Move...
    if lastPlayer == 'black' and win == False:
        return 'white'
    elif lastPlayer == 'white' and win == False:
        return 'black'
    elif lastPlayer == 'black' and win == True:
        return 'black'
    else:
        return 'white'
