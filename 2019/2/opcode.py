#!/usr/bin/env python3
import sys

class opcode(object):
    def __init__(self, fname):
        with open(fname) as f:
            self.n = list(map(lambda x: int(x), f.readline().split(',')))
    
    def calc(self, noun, verb):
        ncp = self.n.copy()
        ncp[1], ncp[2] = noun, verb
        result = None
        i = 0
        while i < len(ncp):
            op = ncp[i]
            if op == 1:
                ncp[ncp[i+3]] = ncp[ncp[i+1]] + ncp[ncp[i+2]]
                i += 4
            elif op == 2:
                ncp[ncp[i+3]] = ncp[ncp[i+1]] * ncp[ncp[i+2]]
                i += 4
            elif op == 99:
                i = len(ncp)
            else: 
                i += 1
        result = ncp[0]
        return result

if __name__ == "__main__":
    op = opcode("input")
    expected_output = 19690720
    for i in range(100):
        for j in range(100):
            r = op.calc(i, j)
            if r == expected_output:
                print(100 * i + j)
                sys.exit(0)



