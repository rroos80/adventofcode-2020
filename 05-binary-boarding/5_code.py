#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

def get_row(code):
    min = 0
    max = 127
    for c in code[:-3]:
        if c == 'F':
            max = max - (max-min+1)/2
        else:
            min = min + (max-min+1)/2

    if min != max:
        print('Error')
        exit(2)
    return(int(min))

def get_column(code):
    min = 0
    max = 7
    for c in code[7:]:
        if c == 'L':
            max = max - (max-min+1)/2
        else:
            min = min + (max-min+1)/2

    if min != max:
        print('Error')
        exit(2)
    return(int(min))


if __name__ == "__main__":

    # First half of the puzzle
    f = open("5_input.txt")
    max_id = 0
    line = f.readline().rstrip()
    
    while (line):
        row = get_row(line)
        col = get_column(line)
        id  = row * 8 + col
        if id > max_id:
            max_id = id
        
        line = f.readline().rstrip()

    f.close()
    print(max_id)
    
    # Second half of the puzzle
    f = open("5_input.txt")
    ids = []
    line = f.readline().rstrip()
    
    while (line):
        row = get_row(line)
        col = get_column(line)
        id  = row * 8 + col
        ids += [id]
     
        line = f.readline().rstrip()
        
    f.close()
    
    for i in ids:
        for j in ids:
            if abs(i-j) == 2:
                temp = 0
                for k in ids:
                    if ((i+1 == k) and (j-1 == k)) or ((j+1 == k) and (i-1 == k)):
                        temp = k
                if temp == 0:
                    result = min(i,j)+1
    print(result)