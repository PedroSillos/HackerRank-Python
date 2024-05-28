n,m = map( int, input().split() )

for i in range(n):
    #print(i)
    center_string = ''
    
    if i == 0 or i == n-1:
        center_string = '.|.'
        
    elif i == (n-1)/2:
        center_string = 'WELCOME'
        
    else:
        if i < (n-1)/2:
            center_string = '.'
            for j in range(i):
                if j == 0:
                    center_string = center_string + '|..|..|'
                else:
                    center_string = center_string + '..|..|'
            center_string = center_string + '.'
        else:
            center_string = '.'
            for j in range(i, n-1):
                if j == i:
                    center_string = center_string + '|..|..|'
                else:
                    center_string = center_string + '..|..|'
            center_string = center_string + '.'

    print(center_string.center(m,'-'))
                
    # ---------------.|.---------------
    # ------------.|..|..|.------------
    # ---------.|..|..|..|..|.---------
    # ------.|..|..|..|..|..|..|.------
    # ---.|..|..|..|..|..|..|..|..|.---
    # -------------WELCOME-------------
    # ---.|..|..|..|..|..|..|..|..|.---
    # ------.|..|..|..|..|..|..|.------
    # ---------.|..|..|..|..|.---------
    # ------------.|..|..|.------------
    # ---------------.|.---------------
