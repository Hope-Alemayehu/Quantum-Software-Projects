# Grover's Algorithm for "Less Than k" Problem

This repository contains Python code implementing Grover's algorithm to solve the "less than k" problem using Qiskit, an open-source quantum computing framework developed by IBM.

## Problem Statement
Given a list of integers, the goal is to find all the integers in the list that are less than a specified value, k.

## Quantum Circuit Components
1. **Oracle**: Marks the states representing numbers less than k.
2. **Inversion About the Mean**: Amplifies the amplitude of the marked states.
3. **Grover Iteration**: Combines the oracle and inversion about the mean operations.

## Code Structure
- `oracle`: Defines the oracle to mark the states representing numbers less than k.
- `inversion_about_mean`: Defines the inversion about the mean operation.
- `grover_iteration`: Defines the function to apply Grover's iteration.
- `less_than_k`: Runs Grover's algorithm for the "less than k" problem.
- Example inputs and simulation of the quantum circuit.

## Usage
1. **Setup Environment**: Ensure you have Python installed along with Qiskit.
2. **Clone Repository**: Clone this repository to your local machine.
    ```bash
    git clone https://github.com/yourusername/quantum-grover-less-than-k.git
    ```
3. **Run Code**: Execute the provided Python script in your preferred Python environment.
    ```bash
    python grover_less_than_k.py
    ```
4. **Interpret Results**: View the histogram plot generated, which represents the counts of measured outcomes.

## Example
```python
k = 7
num_list = [4, 9, 11, 14, 1, 13, 6, 15]
circuit = less_than_k(k, num_list)
## Expected Output
After running the provided example, you should see a histogram plot displaying the counts of measured outcomes, indicating the integers in the input list that are less than the specified value, k.

## Dependencies
- Qiskit
- Matplotlib (for plotting)

## Contributors
- Hope Alemayehu (https://github.com/Hope-Alemayehu)

## Acknowledgments
We would like to thank the [Qiskit](https://qiskit.org/documentation/) team for their valuable contributions to the field of quantum computing.

## Additional Information
For more details on Grover's algorithm and its application to the "less than k" problem, as well as further discussions on quantum computing, feel free to explore the provided source code and related documentation.

