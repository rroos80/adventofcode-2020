#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

if __name__ == "__main__":
    # First half of the puzzle
    f = open("2_input.txt")
    line = f.readline()
    result = 0
    
    while (line):

        l = line.split(' ')
        [min, max] = l[0].split('-')
        [min, max] = [int(min), int(max)]
        letter = l[1][0]
        password = l[2].rstrip()
        
        count = password.count(letter)
        
        if (min <= count <= max):
            result += 1

        line = f.readline()

    f.close()
    print(result)

    # Second half of the puzzle
    f = open("2_input.txt")
    line = f.readline()
    result = 0
    
    while (line):

        l = line.split(' ')
        [first, second] = l[0].split('-')
        [first, second] = [int(first), int(second)]
        letter = l[1][0]
        password = l[2].rstrip()
        
        if ((password[first-1] == letter) ^ (password[second-1] == letter)):
            result += 1

        line = f.readline()
        if line == None:
            f.close()
            break

    print(result)