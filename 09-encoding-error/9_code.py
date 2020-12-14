#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

def validate_value(cipher, val):

    for i in cipher:
        for j in cipher:
            if (val == i+j):
                return None
    return val


if __name__ == "__main__":

    # First half of the puzzle
    data = []
    f = open("9_input.txt")
    line = f.readline()
    
    while (line):
       
        line = line.rstrip()
        data.append(int(line))
        line = f.readline()

    f.close()
    
    cipher = data[:25]
    for i in data[25:]:
        result = validate_value(cipher, i)
        if not result:
            #Remove first item in the cipher and add the new cipher value
            cipher.pop(0)
            cipher.append(i)
        else:
            break

    print(f"The first value in the list that does not comform to the cipher is {result}.")
        
    # Second half of the puzzle
    to_find = result
    temp_total = 0
    temp_values = []
    found = []
    data2 = list(data[:data.index(result)])
    
    for s in range(len(data2)):
        for i in data2[s:len(data2)]:
            temp_total += i
            temp_values += [i]
            if temp_total == to_find:
                found += [temp_values]
                break
            elif temp_total > to_find:
                break
        #print(temp_values)
        temp_total = 0
        temp_values = []
    
    print(f"Found {len(found)} contiguous sets of at least two numbers that sum to {to_find} with the following values:")
    for f in found:
        print(f"  - Smallest value {min(f)}, largest value {max(f)}, sum being {min(f) + max(f)}.")
