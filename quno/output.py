# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 12:10:25 2020

@author: Sebastian
"""

from qiskit.quantum_info import Statevector

def getProbabilityOutput(circuit):
    probabilities = Statevector.from_instruction(circuit).probabilities_dict()
    probabilityOutput = "Probability distribution: "
    for probability in probabilities.items():
        x, y = eval(probability.__str__())
        probabilityOutput += "["
        for c in str(x):
            probabilityOutput+= c + ", "
        probabilityOutput = probabilityOutput[0:len(probabilityOutput)-2]
        probabilityOutput += "] , " + str(round(y, 3)) + "; "
    return probabilityOutput

def getCircuitDrawn(circuit):
    return circuit.draw()
    
def output(probabilityOutput):
    print(probabilityOutput)
    
