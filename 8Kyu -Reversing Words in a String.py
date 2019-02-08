def reverse(st):
    # Your Code Here
    new_li = st.split()
    new_str = ''
    for word in reversed(new_li):
        new_str = new_str + ' ' + word
    return new_str.strip()
