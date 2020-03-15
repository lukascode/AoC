#!/usr/bin/env python3
import sys

class opcode2(object):
    def __init__(self, fname):
        with open(fname) as f:
            self.n = list(map(lambda x: int(x), f.readline().split(',')))
    
    def diagnostic_test(self):
        ncp = self.n.copy()
        i = 0
        while i < len(ncp):
            op = ncp[i]
            if op == 1:
                ncp[ncp[i+3]] = ncp[ncp[i+1]] + ncp[ncp[i+2]]
                i += 4
            elif op == 2:
                ncp[ncp[i+3]] = ncp[ncp[i+1]] * ncp[ncp[i+2]]
                i += 4
            elif op == 3:
                inp = int(input())
                ncp[ncp[i+1]] = inp
                i += 2
            elif op == 4:
                print(ncp[ncp[i+1]])
                i += 2
            elif op == 104:
                print(ncp[i+1])
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

if __name__ == "__main__":
    op = opcode2("input")
    op.diagnostic_test()




