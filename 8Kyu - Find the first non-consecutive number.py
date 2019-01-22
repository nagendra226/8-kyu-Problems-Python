def first_non_consecutive(arr):
    #your code here
    num = arr[0]
    new_num = ''
    for i in arr:
        if i == num:
            num = num + 1
        else:
            new_num = str(i)
            break
    if len(new_num)>0:
        return int(new_num)
    elif new_num=='':
        return None
