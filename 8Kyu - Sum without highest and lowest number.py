def sum_array(arr):
    #your code here
    if(arr==[] or arr==None or len(arr)<=2):
        return 0
    else:
        new_arr = arr
        new_arr.remove(min(arr))
        new_arr.remove(max(arr))
        return sum(new_arr)
