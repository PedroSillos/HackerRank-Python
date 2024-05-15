def swap_case(s):
    new_string = ''
    for char in s:
        if char.isupper():
            new_string = new_string+char.lower()
        else :
            new_string = new_string+char.upper()
    return new_string