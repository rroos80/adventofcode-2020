#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

def breakdown_bag(entry):
    #Remote trailing dot
    entry = entry[:-1]
    #Find first instance of 'bags'
    bag = entry[:entry.index('bags')-1]
    contains = entry[entry.index('contain')+8:]
    contains = contains.split(',')
    contents = {}

    for c in contains:
        temp = c.split(' ')
        if temp[0] == '':
            temp.pop(0)
        
        if temp[0] == 'no':
            break
            
        n = int(temp[0])

        temp.pop(0)
        temp.pop(len(temp)-1)
        contents[' '.join(temp)] = n
    
    return(bag, contents)

def find_bag(bags, to_find, current_bag):
    if current_bag == to_find:
        return 1
    
    if bags.get(current_bag) == {}:
        return 0
    else:
        count = []
        for i, j in bags[current_bag].items():
            count.append(find_bag(bags, to_find, i))
        return max(count)

def count_bag(bags, current_bag, count):
    if bags.get(current_bag) == {}:
        return 0
    else:
        for i, j in bags[current_bag].items():
            count += j+j*count_bag(bags, i, 0)
        return count

        
if __name__ == "__main__":

    # First half of the puzzle
    f = open("7_input.txt")
    bags = {}
    bag_types = []
    line = f.readline()
    
    while (line):
       
        line = line.rstrip()
        
        (bag, contents) = breakdown_bag(line)
        bags[bag] = contents
        bag_types += [bag]
                
        line = f.readline()

    f.close()
    
    count = 0
    my_bag = "shiny gold"
    for i, j in bags.items():
        if i != my_bag:
            count+=find_bag(bags, my_bag, i)
    print(f"{count} bags can contain a {my_bag} bag.")
    
    # Second half of the puzzle
    f = open("7_input.txt")
    bags = {}
    bag_types = []
    line = f.readline()
    
    while (line):
       
        line = line.rstrip()
        
        (bag, contents) = breakdown_bag(line)
        bags[bag] = contents
        bag_types += [bag]
                
        line = f.readline()

    f.close()
    
    #bags = {'shiny gold': {'dark red': 2}, 'dark red': {'dark orange': 2}, 'dark orange': {'dark yellow': 2}, 'dark yellow': {'dark green': 2}, 'dark green': {'dark blue': 2}, 'dark blue': {'dark violet': 2}, 'dark violet': {}}
    
    count = 0
    my_bag = "shiny gold"
    count = count_bag(bags, my_bag, count)
    print(f"{my_bag} bags contain {count} bags.")
