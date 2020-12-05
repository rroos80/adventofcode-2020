#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

def update_record(record, data):
    temp = data.split(' ')
    for d in temp:
        [k, v] = d.split(':')
        record[k] = v
        
    return(record)

def validate_byr(val):
    if 1920 <= int(val) <= 2002:
        return True
    else:
        return False

def validate_iyr(val):
    if 2010 <= int(val) <= 2020:
        return True
    else:
        return False

def validate_eyr(val):
    if 2020 <= int(val) <= 2030:
        return True
    else:
        return False

def validate_hgt(val):
    if val[-2:] == 'cm':
        min = 150
        max = 193
    elif val[-2:] == 'in':
        min = 59
        max = 76
    else:
        return False
    
    if min <= int(val[:-2]) <= max:
        return True
    else:
        return False

def validate_hcl(val):
    if val[0] == '#':
        if len(val[1:])==6:
            for i in val[1:]:
                if i not in '0123456789abcdef':
                    return False
            return True           
    
def validate_ecl(val):
    if val in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return True
    else:
        return False
        
def validate_pid(val):
    if len(val) == 9:
        for i in val:
            if i not in '0123456789':
                return False
        return True
    else:
        return False


def validate_record1(record):
    result = 0
    valid_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for vk in valid_keys:
        if vk in record:
            result += 1
    
    if result > 6:
        return True
    else:
        return False
        
def validate_record2(record):
    result = 0
    valid_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for vk in valid_keys:
        if vk in record:
            if vk == 'byr':
                if validate_byr(record[vk]):
                    result += 1
            if vk == 'iyr':
                if validate_iyr(record[vk]):
                    result += 1
            if vk == 'eyr':
                if validate_eyr(record[vk]):
                    result += 1
            if vk == 'hgt':
                if validate_hgt(record[vk]):
                    result += 1
            if vk == 'hcl':
                if validate_hcl(record[vk]):
                    result += 1
            if vk == 'ecl':
                if validate_ecl(record[vk]):
                    result += 1
            if vk == 'pid':
                if validate_pid(record[vk]):
                    result += 1
    
    if result > 6:
        return True
    else:
        return False
        

if __name__ == "__main__":

    # First half of the puzzle
    f = open("4_input.txt")
    line = f.readline()
    record = {}
    result = 0
    
    while (line):
    
        line = line.rstrip()
        if line == '':
            if validate_record1(record) == True:
                result += 1
            record = {}
        else:
            record = update_record(record, line)
        
        line = f.readline()

    if validate_record1(record) == True:
        result += 1
            
    f.close()
    print(result)

    # Second half of the puzzle
    f = open("4_input.txt")
    line = f.readline()
    record = {}
    result = 0
    
    while (line):
        line = line.rstrip()
        if line == '':
            if validate_record2(record) == True:
                result += 1
            record = {}
        else:
            record = update_record(record, line)
        
        line = f.readline()

    if validate_record2(record) == True:
        result += 1
            
    f.close()
    print(result)