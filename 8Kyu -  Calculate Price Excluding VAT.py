def excluding_vat_price(price):
    if price == '' or price == 0 or price == None:
        return -1
    else: 
        price = price/1.15
        return round(price,2)
