def fillable(stock, merch, n):
    # Your code goes here.
    try:
        return stock[merch]>=n
    except:
        return False
