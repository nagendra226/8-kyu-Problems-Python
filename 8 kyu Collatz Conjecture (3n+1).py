def hotpo(n):
    count = 0
    if n == 1:
        return 0
    else:
        while True:
            if n%2 == 0:
                n = n/2
                count = count +1
            else:
                n = 3 * n + 1
                count = count + 1
                
            if(n==1):
                False
                break
    return count
              
                
