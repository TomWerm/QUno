# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 12:27:21 2020

@author: Sebastian
"""

from qiskit import *

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
    x, y = eval(counts.__str__())
    return counts.__str__()