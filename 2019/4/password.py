#!/usr/bin/env python3


def check_pass(p):
    p = str(p)
    if len(p) != 6:
        return False
    double = False
    for i in range(len(p)):
        if i > 0:
            if p[i] < p[i-1]:
                return False
            if p[i] == p[i-1]:
                if (i + 1 < len(p)) and (p[i + 1] == p[i]):
                    pass
                elif (i - 2 >= 0) and (p[i-2] == p[i]):
                    pass
                else:
                    double = True
    return double
        

def count_pass(_from, _to):
    i, result = _from, 0
    while i <= _to:
        if check_pass(i):
            result += 1
        i += 1
    return result

r = count_pass(136818, 685979)
print(r)