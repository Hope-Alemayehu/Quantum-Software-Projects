#!/usr/bin/env python
# coding: utf-8

# In[14]:


from qiskit import QuantumCircuit, Aer, transpile, assemble
from math import sqrt

# Define the set of numbers (no duplicates)
numbersSet = {5, 8, 2, 10, 7, 4, 3, 1, 9, 6}
number = [5, 8, 2, 10, 7, 4, 3, 1, 9, 6]

# Prompt the user to submit a number
target_number = int(input("Submit a number: "))

# Check if the submitted number is in the set
if target_number not in numbersSet:
    print(f"There is no number {target_number} in the set.")
else:
    # Determine the number of qubits required to represent the numbers
    num_qubits = len(numbers).bit_length()

    # Number of iterations for Grover's algorithm (approximately sqrt(N))
    num_iterations = round(sqrt(len(numbers)))

    # Create a quantum circuit
    qc = QuantumCircuit(num_qubits)

    # Apply Hadamard gates to all qubits
    qc.h(range(num_qubits))

    # Apply Oracle to mark the state corresponding to the target number
    oracle = QuantumCircuit(num_qubits)
    for index, number in enumerate(numbers):
        if number == target_number:
            binary_index = format(index, f'0{num_qubits}b')
            for qubit_index, bit in enumerate(binary_index):
                if bit == '1':
                    oracle.x(qubit_index)

    oracle.h(range(num_qubits))
    oracle.z(range(num_qubits))
    for index, number in enumerate(numbers):
        if number == target_number:
            binary_index = format(index, f'0{num_qubits}b')
            for qubit_index, bit in enumerate(binary_index):
                if bit == '1':
                    oracle.x(qubit_index)

    qc = qc.compose(oracle)

    # Apply Grover diffusion operator
    qc.h(range(num_qubits))
    qc.z(range(num_qubits))
    qc.cz(0, num_qubits - 1)
    qc.h(range(num_qubits))

    # Measure qubits
    qc.measure_all()

    # Simulate the circuit
    simulator = Aer.get_backend('qasm_simulator')
    transpiled_qc = transpile(qc, simulator)
    qobj = assemble(transpiled_qc,  shots=2000)
    result = simulator.run(qobj).result()

    # Convert binary index to decimal
    def binary_to_decimal(binary_str):
        return int(binary_str, 2)

    # Convert binary index to decimal for each outcome
    counts = result.get_counts()
    total_counts = sum(counts.values())

    # Print candidate answers with probabilities
    print("\nCandidate Answers with Probabilities:")
    for index, count in counts.items():
        probability = count / total_counts
        print(f"{index}: {probability:.4f}")


# In[ ]:





# In[ ]:




