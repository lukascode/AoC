#!/usr/bin/env python3

### Complete IntCode computer

import sys
import itertools
from queue import Queue

class Opcode:

    opcodes = {
        0: None,
        1: 3,
        2: 3,
        3: 1,
        4: 1,
        5: 2,
        6: 2, 
        7: 3,
        8: 3,
        9: 1,
        99: 0
    }

    def __init__(self, opcode):
        self.op = None
        self.modes = []
        self.__parse_opcode(opcode)

    def get_opcode(self):
        return self.op
        
    def get_mode(self, param):
        nofparams = Opcode.opcodes[self.op]
        if param > nofparams or param < 1:
            raise ValueError("Invalid opcode param number")
        return self.modes[len(self.modes) - param]
    
    def __parse_opcode(self, opcode):
        opcode = str(opcode)
        if len(opcode) == 0:
            raise ValueError("Invalid opcode")
        elif len(opcode) > 2:
            op = int(opcode[len(opcode)-2:])
        else:
            op = int(opcode)
        self.__validate_opcode(op)
        self.op = op
        nofparams = Opcode.opcodes[self.op]
        modes = '0' * nofparams
        if len(opcode) > 2:
            m = opcode[:len(opcode)-2]
            modes = modes[0:len(modes)-len(m)] + m
        self.modes = [int(i) for i in modes]

    def __validate_opcode(self, op):
        if op not in Opcode.opcodes:
            raise ValueError("Opcode not supported")
            



class IntCode:

    code = None

    def __init__(self, phase_input):
        self.inputs = Queue()
        self.outputs = []
        self.add_input(phase_input)

    def add_input(self, _input):
        self.inputs.put(_input)
    
    def get_input(self):
        return self.inputs.get()
    
    def has_input(self):
        return not self.inputs.empty()

    def add_output(self, _output):
        self.outputs.append(_output)
        
    def run_program(self):
        self.ncp = IntCode.code.copy()
        self.ncp.extend([0 for i in range(2000)])
        self.i = 0
        self.relative_base = 0
        while self.i < len(self.ncp):
            op = self.ncp[self.i]
            if op != 0:
                opcode = Opcode(op)
                self.__process_opcode(opcode)
            else:
                break
            
    
    def __process_opcode(self, opcode):
        op = opcode.get_opcode()
        if op == 1:
            self.__add(opcode)
        elif op == 2:
            self.__mul(opcode)
        elif op == 3:
            self.__in(opcode)
        elif op == 4:
            self.__out(opcode)
        elif op == 5:
            self.__jump_if_true(opcode)
        elif op == 6:
            self.__jump_if_false(opcode)
        elif op == 7:
            self.__less_than(opcode)
        elif op == 8:
            self.__equals(opcode)
        elif op == 9:
            self.__adjust_rbase(opcode)
        elif op == 99:
            self.i = len(self.ncp)
        else:
            raise ValueError("Opcode not supported")
    
    def __add(self, opcode):
        param1 = self.__get_param_value(opcode, 1)
        param2 = self.__get_param_value(opcode, 2)
        self.__store_value(opcode, param1 + param2, 3)
        self.i += 4
    
    def __mul(self, opcode):
        param1 = self.__get_param_value(opcode, 1)
        param2 = self.__get_param_value(opcode, 2)
        self.__store_value(opcode, param1 * param2, 3)
        self.i += 4

    def __in(self, opcode):
        if self.has_input():
            inp = self.get_input()
            self.__store_value(opcode, inp, 1)
        self.i += 2
    
    def __out(self, opcode):
        param1 = self.__get_param_value(opcode, 1)
        self.add_output(param1)
        self.i += 2
    
    def __jump_if_true(self, opcode):
        param1 = self.__get_param_value(opcode, 1)
        if param1 != 0:
            param2 = self.__get_param_value(opcode, 2)
            self.i = param2
        else:
            self.i += 3
    
    def __jump_if_false(self, opcode):
        param1 = self.__get_param_value(opcode, 1)
        if param1 == 0:
            param2 = self.__get_param_value(opcode, 2)
            self.i = param2
        else:
            self.i += 3

    def __less_than(self, opcode):
        param1 = self.__get_param_value(opcode, 1)
        param2 = self.__get_param_value(opcode, 2)
        if param1 < param2:
            self.__store_value(opcode, 1, 3)
        else: 
            self.__store_value(opcode, 0, 3)
        self.i += 4

    def __equals(self, opcode):
        param1 = self.__get_param_value(opcode, 1)
        param2 = self.__get_param_value(opcode, 2)
        if param1 == param2:
            self.__store_value(opcode, 1, 3)
        else: 
            self.__store_value(opcode, 0, 3)
        self.i += 4
    
    def __adjust_rbase(self, opcode):
        param1 = self.__get_param_value(opcode, 1)
        self.relative_base += param1
        self.i += 2

    def __get_param_value(self, opcode, param):
        if param > 0:
            mode = opcode.get_mode(param)
            if mode == 0:
                return self.ncp[self.ncp[self.i + param]]
            elif mode == 1:
                return self.ncp[self.i + param]
            elif mode == 2:
                return self.ncp[self.relative_base + self.ncp[self.i + param]]
            else:
                raise ValueError("Mode not supported")
        else:
            raise ValueError("Bad parameter")

    def __store_value(self, opcode, value, param):
        if param > 0:
            mode = opcode.get_mode(param)
            if mode == 0:
                addr = self.ncp[self.i + param]
            elif mode == 2:
                addr = self.relative_base + self.ncp[self.i + param]
            else:
                raise ValueError("Mode not supported");
            self.ncp[addr] = value
        else:
            raise ValueError("Bad parameter")

if __name__ == "__main__":
    with open("input") as f:
        IntCode.code = list(map(lambda x: int(x), f.readline().split(',')))
        
        program = IntCode(2)
        program.run_program()

        print(program.outputs)
