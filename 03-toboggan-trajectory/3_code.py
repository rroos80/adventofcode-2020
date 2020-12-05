#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

def do_slope(r, d):
    f = open("3_input.txt")
    line = f.readline()
    i = 0
    j = 0
    result = 0
    
    while (line):

        if line[j] == '#':
            temp = line[:j]+'X'+line[j+1:]
            result += 1
        else:
            temp = line[:j]+'O'+line[j+1:]
        
        j += r
        if j>30:
            j -= 31
        
        for k in range(d):
            line = f.readline()

    f.close()
    return(result)


if __name__ == "__main__":
    # First half of the puzzle
    print(do_slope(3,1))
    # Second half of the puzzle
    print(do_slope(1, 1)*do_slope(3, 1)*do_slope(5, 1)*do_slope(7, 1)*do_slope(1, 2))
