def stairs_in_20(stairs):
    total_sum = 0
    length_arr = len(stairs)
    for i in range(0,length_arr):
        total_sum = total_sum + sum(stairs[i])
    return total_sum*20
