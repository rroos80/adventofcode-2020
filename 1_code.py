#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

if __name__ == "__main__":
    f = open("1_input.txt")
    l = f.readline()
    a = []
    while (l):
        l = f.readline()
        if l:
            a += [int(l)]
    f.close()

    # First half of the puzzle
    for i in a:
        for j in a:
                if ((i+j)==2020):
                    result = i * j
    print(result)
    
    # Second half of the puzzle
    for i in a:
        for j in a:
            for k in a:
                if ((i+j+k)==2020):
                    result = i*j*k
    print(result)  