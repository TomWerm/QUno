from enum import Enum
from math import pi

class Card:
    def __init__(self, gate):
        self.gate = gate

class Gate(Enum):
    h = 1
    x = 2
    cx = 3
    ccx = 4
    swap = 5
    cswap = 6
    rx = 13
    ry = 14
    rz = 15
    u3 = 16
    y = 17
    u2 = 18
    ch = 19
    cy = 20
    cz = 21
    crx = 22
    cry = 23
    crz = 24
    cu1 = 23
    cu3 = 24
    rxx = 27
    rzz = 28

    def get(self):
        return self.name
    
    def getParamCount(self):
        if self == Gate.h:
            return 1
        elif self == Gate.x:
            return 1
        elif self == Gate.cx:
            return 2
        elif self == Gate.ccx:
            return 3
        elif self == Gate.swap:
            return 2
        elif self == Gate.cswap:
            return 3
        elif self == Gate.rx:
            return 1
        elif self == Gate.ry:
            return 1
        elif self == Gate.rz:
            return 1
        elif self == Gate.u3:
            return 1
        elif self == Gate.y:
            return 1
        elif self == Gate.u2:
            return 1
        elif self == Gate.ch:
            return 2
        elif self == Gate.cy:
            return 2
        elif self == Gate.cz:
            return 2
        elif self == Gate.crx:
            return 2
        elif self == Gate.cry:
            return 2
        elif self == Gate.crz:
            return 2
        elif self == Gate.cu1:
            return 2
        elif self == Gate.cu3:
            return 2        
        elif self == Gate.rxx:
            return 2
        elif self == Gate.rzz:
            return 2

def addGateToCircuit(circuit, gate, params):
    if gate == Gate.h:
        circuit.h(params[0])
    elif gate == Gate.x:
        circuit.x(params[0])
    elif gate == Gate.cx:
        circuit.cx(params[0], params[1])
    elif gate == Gate.ccx:
        circuit.ccx(params[0], params[1], params[2])
    elif gate == Gate.swap:
        circuit.swap(params[0], params[1])
    elif gate == Gate.cswap:
        circuit.cswap(params[0], params[1], params[2])
    elif gate == Gate.rx:
        circuit.rx(pi/2, params[0])
    elif gate == Gate.ry:
        circuit.ry(pi/2, params[0])
    elif gate == Gate.rz:
        circuit.rz(pi/2, params[0])
    elif gate == Gate.u3:
        circuit.u3(pi/2, pi/2, pi/2, params[0])
    elif gate == Gate.y:
        circuit.y(params[0])
    if gate == Gate.u2:
        circuit.u2(pi/2, pi/2, params[0])
    elif gate == Gate.ch:
        circuit.ch(params[0], params[1])
    elif gate == Gate.cy:
        circuit.cy(params[0], params[1])
    elif gate == Gate.cz:
        circuit.cz(params[0], params[1])
    elif gate == Gate.crx:
        circuit.crx(pi/2, params[0], params[1])
    elif gate == Gate.cry:
        circuit.cry(pi/2, params[0], params[1])
    elif gate == Gate.crz:
        circuit.crz(pi/2, params[0], params[1])
    elif gate == Gate.cu1:
        circuit.cu1(pi/2, params[0], params[1])
    elif gate == Gate.cu3:
        circuit.cu3(pi/2, pi/2, pi/2, params[0], params[1])
    elif gate == Gate.rxx:
        circuit.rxx(pi/2, params[0], params[1])
    elif gate == Gate.rzz:
        circuit.rzz(pi/2, params[0], params[1])