#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

def get_count1(group):
    unique = []
    for i in group:
        if i not in unique:
            unique += i
    return(len(unique))
        
def get_count2(group):
    unique = 0
    for i in group[0]:
        n = 0
        for j in group:
            if i in j:
                n += 1
        if n == len(group):
            unique += 1
        
    return(unique)
        

if __name__ == "__main__":

    # First half of the puzzle
    f = open("6_input.txt")
    group = []
    total_count = 0
    line = f.readline()
    
    while (line):
       
        line = line.rstrip()
        
        if line == '':
            count = get_count1(group)
            total_count += count
            group = []
        else:
            group += line
            
        line = f.readline()

    f.close()
    
    count = get_count1(group)
    total_count += count
    print(total_count)
    
    # Second half of the puzzle
    f = open("6_input.txt")
    group = []
    total_count = 0
    line = f.readline()
    
    while (line):
       
        line = line.rstrip()
        
        if line == '':
            count = get_count2(group)
            total_count += count
            group = []
        else:
            group += [line]
            
        line = f.readline()

    f.close()
    
    count = get_count2(group)
    total_count += count
    print(total_count)
