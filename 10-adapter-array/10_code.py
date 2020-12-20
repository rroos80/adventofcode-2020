#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

def select(adapters, active_joltage, memo = {}):
    if active_joltage == max(adapters):
        return 1
    
    if active_joltage in memo:
        return memo[active_joltage]
 
    # Find suitable adapters that work with the current joltage output
    suitable_adapters = []
    for i in adapters:
        if active_joltage < i <= active_joltage + 3:
            suitable_adapters.append(i)
    if len(suitable_adapters) == 0:
        return 0
    
    count = 0
    for i in suitable_adapters:  
        count += select(adapters, i, memo)
    memo[active_joltage] = count
    return count


if __name__ == "__main__":

    # First half of the puzzle
    raw_data = []
    f = open("10_input.txt")
    line = f.readline()
    
    while (line):
        line = line.rstrip()
        raw_data.append(int(line))
        line = f.readline()
    f.close()
    
    # Maximum device rating is 3 higher than the highest adapters. Add this one to the data to work through.
    data = raw_data.copy()
    device_max = max(data)+3
    data.append(device_max)
    
    # Start with joltage 0 and sort the list for easy debugging
    active_joltage = 0
    selected_diff_list = []

    while (len(data)>0):
        # Find suitable adapters that work with the current joltage output
        suitable_adapters = []
        for i in data:
            if i <= active_joltage + 3:
                suitable_adapters.append(i)
        if len(suitable_adapters) == 0:
            print('Panic: no suitable adapters for current joltage detected')
            exit(2)
        selected = min(suitable_adapters)
        selected_diff_list.append(selected-active_joltage)
        active_joltage += selected - active_joltage
        data.remove(selected)
    
    count_diff_one = selected_diff_list.count(1)
    count_diff_three = selected_diff_list.count(3)
    print(f"Identified {count_diff_one} times a 1-jolt difference and {count_diff_three} times a 3-jolt difference, which multiplies to {count_diff_one*count_diff_three}.")
    
    # Second half of the puzzle
    data = raw_data
    count = 0
    
    device_max = max(data)+3
    data.append(device_max)
    data.sort()
    count = select(data, 0, {})

    print(f"The total number of ways to arrange the adapters in a valid way is {count}.")
 