def count_substring(string, sub_string):
    count=0
    for i in range( len(string) ):
        match=0
        for j in range( len(sub_string) ):
            if i+j >= len(string):
                break
            #print(string[i+j],sub_string[j])
            if string[i+j] == sub_string[j]:
                match+=1
        #print(match)
        if match == len(sub_string):
            #print('match')
            count+=1
    return count