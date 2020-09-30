# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 2020

@author: Julia Butte, Sebastian Weber, Thomas Weber
"""

from qiskit.quantum_info import Statevector

#Calculate the maesurement probability for the @param circuit and format it
def getProbabilityOutput(circuit):
    #Calculate the maesurement probability
    probabilities = Statevector.from_instruction(circuit).probabilities_dict()
    probabilityOutput = "Probability distribution: "
    
    #Format according to [q0, q1, q2], probabaility; ... for the qbits q0, q1 and q2
    for probability in probabilities.items():
        x, y = eval(probability.__str__())
        probabilityOutput += "["
        for c in str(x):
            probabilityOutput+= c + ", "
        probabilityOutput = probabilityOutput[0:len(probabilityOutput)-2]
        probabilityOutput += "] , " + str(round(y, 3)) + "; "
    return probabilityOutput
    
#Output method 
def output(probabilityOutput):
    print(probabilityOutput)
    
