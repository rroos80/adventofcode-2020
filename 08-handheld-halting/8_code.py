#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

def execute(program, executed = []):
    pc_prev = 0
    pc = 0
    acc = 0
    while(pc not in executed):
        i, arg = program[pc]
        executed += [pc]
        if i == 'jmp':
            pc_prev = pc
            pc += int(arg)
        elif i == 'acc':
            acc += int(arg)
            pc_prev = pc
            pc += 1
        elif i == 'nop':
            pc_prev = pc
            pc += 1
        else:
            #Shouldn't happen
            exit(2)

    return (pc_prev, pc, acc)

if __name__ == "__main__":

    # First half of the puzzle
    program = []
    f = open("8_input.txt")
    line = f.readline()
    
    while (line):
       
        line = line.rstrip()
        i, arg = line.split(' ')
        program.append((i, arg))
        
        line = f.readline()

    f.close()

    pc_prev, pc, acc = execute(program)
    print(f"Accumulator value is {acc} immediately prior to executing an instruction for a second time.")
    
    # Second half of the puzzle
    pc = 0
    pc_new = 0
    for ins, arg in program:
        restore_pc = pc
        if ins == 'jmp':
            restore_ins = ('jmp', arg)
            program[pc] = ('nop', arg)
            pc_prev, pc_new, acc = execute(program, [len(program)])
            program[restore_pc] = restore_ins
        elif ins == 'nop':
            restore_ins = ('nop', arg)
            program[pc] = ('jmp', arg)
            pc_prev, pc_new, acc = execute(program, [len(program)])
            program[restore_pc] = restore_ins
        else:
            pass
        if pc_new == len(program):
            break
        pc += 1

    print(f"Changing instruction {ins} at PC {pc} ensures the program executes at PC {pc_new} with accumulator value {acc}.")