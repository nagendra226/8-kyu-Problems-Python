def rain_amount(mm):
    x = 40 - mm
    if (mm < 40):
         return "You need to give your plant {}".format(x)+ "mm of water"
    else:
         return "Your plant has had more than enough water for today!"
