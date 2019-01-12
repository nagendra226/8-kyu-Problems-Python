def char_freq(message):
    d = {}
    for i in sorted(message):
            d[i] = message.count(i)
    return d
            
