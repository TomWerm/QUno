from enum import Enum

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
    cu1 = 25
    cu3 = 26
    rxx = 27
    rzz = 28

    def get(self):
        return self.name
    
    def getParamCount(self):
        if self.gate == Gate.h:
            return 1
        elif self.gate == Gate.x:
            return 1
        elif self.gate == Gate.cx:
            return 1
        elif self.gate == Gate.ccx:
            return 2
        elif self.gate == Gate.swap:
            return 2
        elif self.gate == Gate.cswap:
            return 3
        elif self.gate == Gate.rx:
            return 1
        elif self.gate == Gate.ry:
            return 1
        elif self.gate == Gate.rz:
            return 1
        elif self.gate == Gate.u3:
            return 1
        elif self.gate == Gate.y:
            return 1
        elif self.gate == Gate.u2:
            return 1
        elif self.gate == Gate.ch:
            return 2
        elif self.gate == Gate.cy:
            return 2
        elif self.gate == Gate.cz:
            return 2
        elif self.gate == Gate.crx:
            return 2
        elif self.gate == Gate.cry:
            return 2
        elif self.gate == Gate.crz:
            return 2
        elif self.gate == Gate.cu1:
            return 2
        elif self.gate == Gate.cu3:
            return 2
        elif self.gate == Gate.rxx:
            return 2
        elif self.gate == Gate.rzz:
            return 2

def addGateToCircuit(circuit, gate, params):
    if gate == Gate.h:
        circuit.h(params[0])
    elif gate == Gate.x:
        circuit.x(params[0])
    elif gate == Gate.cx:
        circuit.cx(params[0], params[1])
    elif gate == Gate.ccx:
        circuit.ccx(params[0], params[1])
    elif gate == Gate.swap:
        circuit.swap(params[0], params[1])
    elif gate == Gate.cswap:
        circuit.cswap(params[0], params[1], params[2])
    elif gate == Gate.rx:
        circuit.rx(params[0])
    elif gate == Gate.ry:
        circuit.ry(params[0])
    elif gate == Gate.rz:
        circuit.rz(params[0])
    elif gate == Gate.u3:
        circuit.u3(params[0])
    elif gate == Gate.y:
        circuit.y(params[0])
    if gate == Gate.u2:
        circuit.u2(params[0])
    elif gate == Gate.ch:
        circuit.ch(params[0], params[1])
    elif gate == Gate.cy:
        circuit.cy(params[0], params[1])
    elif gate == Gate.cz:
        circuit.cz(params[0], params[1])
    elif gate == Gate.crx:
        circuit.crx(params[0], params[1])
    elif gate == Gate.cry:
        circuit.cry(params[0], params[1])
    elif gate == Gate.crz:
        circuit.crz(params[0], params[1])
    elif gate == Gate.cu1:
        circuit.cu1(params[0], params[1])
    elif gate == Gate.cu3:
        circuit.cu3(params[0], params[1])
    elif gate == Gate.rxx:
        circuit.rxx(params[0], params[1])
    elif gate == Gate.rzz:
        circuit.rzz(params[0], params[1])