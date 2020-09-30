# Importing standard Qiskit libraries and configuring account
from qiskit import QuantumCircuit, execute, Aer, IBMQ
from qiskit.compiler import transpile, assemble
from qiskit.quantum_info import Statevector
from qiskit.visualization import *
from math import sqrt

# Build
#------

initial_state = [0.+1.j/sqrt(2),1/sqrt(2)+0.j]

# Create a Quantum Circuit acting on the q register
circuit = QuantumCircuit(3, 3)

circuit.initialize([0.+1.j/sqrt(2),1/sqrt(2)+0.j], 0)
circuit.initialize([0.+1.j/sqrt(2),1/sqrt(2)+0.j], 1)
circuit.initialize([0.+1.j/sqrt(2),1/sqrt(2)+0.j], 2)


# Add a H gate on qubit 0
circuit.h(0)

# Add a CX (CNOT) gate on control qubit 0 and target qubit 1
circuit.cx(0, 1)

statevector = Statevector.from_instruction(circuit)
print("\nTotal count for 00 and 11 are:",statevector.probabilities_dict())

# Map the quantum measurement to the classical bits
circuit.measure([0,1,2], [0,1,2])

# Execute
#--------

# Use Aer's qasm_simulator
simulator = Aer.get_backend('statevector_simulator')

# Execute the circuit on the qasm simulator
job = execute(circuit, simulator, shots=1000)

# Grab results from the job
result = job.result()

# Return counts
counts = result.get_counts(circuit)
print("\nTotal count for 00 and 11 are:",counts)

# Analyze
#--------

# Draw the circuit
print(circuit.draw())

print(result.get_statevector(0))

# END