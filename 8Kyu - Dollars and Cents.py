def format_money(amount):
    # your formatting code here
    a = amount
    return "${0:.2f}".format(round(a,2))
