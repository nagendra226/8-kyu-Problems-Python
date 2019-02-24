def shortcut( s ):
    # ...
    result = ""
    for i in s:
        if i not in ['a','i','e','o','u']:
            result = result + i
    return result
