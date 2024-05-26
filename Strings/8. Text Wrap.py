
import math

def wrap(string, max_width):
    row_number = int( math.ceil(len(string)/max_width) )
    result = ''
    for i in range(row_number):
        line_result = ''
        for j in range(max_width):
            if (i*max_width)+j < len(string):
                line_result = line_result + string[(i*max_width)+j]
        if i != row_number-1:            
            print(line_result)
        else:
            result=line_result
    return result

