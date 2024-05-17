if __name__ == '__main__':
    s = input()
    
    isalnum = False
    for char in s:
        if char.isalnum():
            isalnum = True
            break
    print(isalnum)
    
    isalpha = False
    for char in s:
        if char.isalpha():
            isalpha = True
            break
    print(isalpha)
    
    isdigit = False
    for char in s:
        if char.isdigit():
            isdigit = True
            break
    print(isdigit)
    
    islower = False
    for char in s:
        if char.islower():
            islower = True
            break
    print(islower)
    
    isupper = False
    for char in s:
        if char.isupper():
            isupper = True
            break
    print(isupper)