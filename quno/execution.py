# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 2020

@author: Julia Butte, Sebastian Weber, Thomas Weber
"""

from qiskit import *

#Run one measurement of the @param circuit and format the result
#Adapted from an example of IBM from https://qiskit.org/documentation/getting_started.html
def calculateResult(circuit):
    
    # Use Aer's qasm_simulator
    simulator = Aer.get_backend('qasm_simulator')
    
    # Map the quantum measurement to the classical bits
    circuit.measure(range(3), range(3))

    # Execute the circuit on the qasm simulator
    job = execute(circuit, simulator, shots=1)

    # Grab results from the job
    result = job.result()

    # Returns counts
    counts = result.get_counts()
    
    #Format according to [q0, q1, q2] with the measured values for the qbits q0, q1 and q2
    for count in counts.items():
        x, y = eval(count.__str__())
        result = "["
        for c in str(x):
            result+= c + ", "
        result = result[0:len(result)-2]
        result += "]"
        return result