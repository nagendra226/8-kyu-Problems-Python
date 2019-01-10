def nba_extrap(ppg, mpg):
    if ppg== 0 or mpg==0:
        return 0
    else:
        return round(ppg * 48 /mpg,1)
