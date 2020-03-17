#!/usr/bin/env python3

import sys
import itertools
from queue import Queue

class amplifier(object):

    code = None

    def __init__(self, phase_input):
        self.pc = 0
        self.halted = False
        self.other_amplifier = None
        self.inputs = Queue()
        self.add_input(phase_input)
        self.outputs = []
    
    def set_other_amplifier(self, other_amplifier):
        self.other_amplifier = other_amplifier
    
    def has_other_amplifier(self):
        return self.other_amplifier is not None

    def add_input(self, _input):
        self.inputs.put(_input)
    
    def get_input(self):
        return self.inputs.get()
    
    def has_input(self):
        return not self.inputs.empty()

    def add_output(self, _output):
        if self.has_other_amplifier() and not self.other_amplifier.halted:
            self.other_amplifier.add_input(_output)
        else:
            self.outputs.append(_output)
        
    def run_program(self):
        ncp = amplifier.code.copy()
        i = self.pc
        while i < len(ncp):
            op = ncp[i]
            if op == 1:
                ncp[ncp[i+3]] = ncp[ncp[i+1]] + ncp[ncp[i+2]]
                i += 4
            elif op == 2:
                ncp[ncp[i+3]] = ncp[ncp[i+1]] * ncp[ncp[i+2]]
                i += 4
            elif op == 3:
                if self.has_input():
                    inp = self.get_input()
                    ncp[ncp[i+1]] = inp
                    i += 2
                else:
                    self.pc = i
                    if self.has_other_amplifier() and not self.other_amplifier.halted:
                        self.other_amplifier.run_program()
                    return
            elif op == 4:
                self.add_output(ncp[ncp[i+1]])
                i += 2
            elif op == 104:
                self.add_output(ncp[i+1])
                i += 2
            elif op == 5: # jump-if-true
                if ncp[ncp[i+1]] != 0:
                    i = ncp[ncp[i+2]]
                else:
                    i += 3
            elif op == 105:
                if ncp[i+1] != 0:
                    i = ncp[ncp[i+2]]
                else:
                    i += 3
            elif op == 1005:
                if ncp[ncp[i+1]] != 0:
                    i = ncp[i+2]
                else:
                    i += 3
            elif op == 1105:
                if ncp[i+1] != 0:
                    i = ncp[i+2]
                else:
                    i += 3
            elif op == 6: # jump-if-false
                if ncp[ncp[i+1]] == 0:
                    i = ncp[ncp[i+2]]
                else:
                    i += 3
            elif op == 106:
                if ncp[i+1] == 0:
                    i = ncp[ncp[i+2]]
                else:
                    i += 3
            elif op == 1006:
                if ncp[ncp[i+1]] == 0:
                    i = ncp[i+2]
                else:
                    i += 3
            elif op == 1106:
                if ncp[i+1] == 0:
                    i = ncp[i+2]
                else:
                    i += 3
            elif op == 7: # less than
                if ncp[ncp[i+1]] < ncp[ncp[i+2]]:
                    ncp[ncp[i+3]] = 1
                else:
                    ncp[ncp[i+3]] = 0
                i += 4
            elif op == 107:
                if ncp[i+1] < ncp[ncp[i+2]]:
                    ncp[ncp[i+3]] = 1
                else:
                    ncp[ncp[i+3]] = 0
                i += 4
            elif op == 1007:
                if ncp[ncp[i+1]] < ncp[i+2]:
                    ncp[ncp[i+3]] = 1
                else:
                    ncp[ncp[i+3]] = 0
                i += 4
            elif op == 1107:
                if ncp[i+1] < ncp[i+2]:
                    ncp[ncp[i+3]] = 1
                else:
                    ncp[ncp[i+3]] = 0
                i += 4
            elif op == 8: # equals 
                if ncp[ncp[i+1]] == ncp[ncp[i+2]]:
                    ncp[ncp[i+3]] = 1
                else:
                    ncp[ncp[i+3]] = 0
                i += 4
            elif op == 108:
                if ncp[i+1] == ncp[ncp[i+2]]:
                    ncp[ncp[i+3]] = 1
                else:
                    ncp[ncp[i+3]] = 0
                i += 4
            elif op == 1008:
                if ncp[ncp[i+1]] == ncp[i+2]:
                    ncp[ncp[i+3]] = 1
                else:
                    ncp[ncp[i+3]] = 0
                i += 4
            elif op == 1108:
                if ncp[i+1] == ncp[i+2]:
                    ncp[ncp[i+3]] = 1
                else:
                    ncp[ncp[i+3]] = 0
                i += 4
            elif op == 101: # addition
                ncp[ncp[i+3]] = ncp[i+1] + ncp[ncp[i+2]]
                i += 4
            elif op == 1001:
                ncp[ncp[i+3]] = ncp[ncp[i+1]] + ncp[i+2]
                i += 4
            elif op == 1101:
                ncp[ncp[i+3]] = ncp[i+1] + ncp[i+2]
                i += 4
            elif op == 102: # multiplication
                ncp[ncp[i+3]] = ncp[i+1] * ncp[ncp[i+2]]
                i += 4
            elif op == 1002:
                ncp[ncp[i+3]] = ncp[ncp[i+1]] * ncp[i+2]
                i += 4
            elif op == 1102:
                ncp[ncp[i+3]] = ncp[i+1] * ncp[i+2]
                i += 4
            elif op == 99:
                i = len(ncp)
            else:
                print(op, "opcode not supported")
                i += 1
        self.halted = True
        if self.has_other_amplifier() and not self.other_amplifier.halted:
            self.other_amplifier.run_program()

def get_signal(permutation_iter):
    a = amplifier(next(permutation_iter))
    a.add_input(0)

    b = amplifier(next(permutation_iter))
    c = amplifier(next(permutation_iter))
    d = amplifier(next(permutation_iter))
    e = amplifier(next(permutation_iter))

    a.set_other_amplifier(b)
    b.set_other_amplifier(c)
    c.set_other_amplifier(d)
    d.set_other_amplifier(e)
    e.set_other_amplifier(a)

    a.run_program()

    return e.outputs

def solve(permutation_base):
    permutations = itertools.permutations(permutation_base)
    max_signal = None
    max_signal_phase_seq = None
    for p in permutations:
        signal = get_signal(iter(p))
        if not max_signal or signal > max_signal:
            max_signal = signal
            max_signal_phase_seq = p
    print(max_signal_phase_seq, '->', max_signal)

if __name__ == "__main__":
    with open("input") as f:
            amplifier.code = list(map(lambda x: int(x), f.readline().split(',')))
    solve([0, 1, 2, 3, 4]) # part1
    solve([5, 6, 7, 8, 9]) # part2
    



