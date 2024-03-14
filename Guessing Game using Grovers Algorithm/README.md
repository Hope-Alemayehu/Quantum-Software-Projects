# Quantum Guessing Game with Grover's Algorithm

## Overview
This project implements a guessing game using Grover's algorithm, a quantum algorithm, to find a specific number from a predefined set of numbers. Grover's algorithm provides a quadratic speedup compared to classical algorithms for this task.

## How it Works
1. **Set of Numbers**: The game is played with a set of numbers. Each number in the set represents a possible answer. (Assumption: There are no duplicate values in the set.)

2. **Guessing Phase**: The player submits a number as a guess.

3. **Quantum Search**: The program utilizes Grover's algorithm to search for the guessed number within the set of numbers.

4. **Result**: The program outputs the candidate indices where the guessed number could potentially be found within the set of numbers. These candidate indices are provided along with their corresponding probabilities based on the quantum search results.

## Requirements
- Python 3.x
- Qiskit: The program relies on the Qiskit library for quantum computing simulations.

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/your_username/quantum-guessing-game.git
    ```
2. Install dependencies:
    ```bash
    pip install qiskit
    ```

## Usage
1. Run the program:
    ```bash
    python quantum_guessing_game.py
    ```
2. Follow the on-screen prompts to submit your guess.

## How to Play
1. Submit a number as your guess.
2. The program will determine if your guess is within the set of numbers.
3. Based on Grover's algorithm, the program will provide candidate indices where the guessed number could potentially be found within the set of numbers. These candidate indices are provided along with their corresponding probabilities.
4. Compare the probabilities to refine your guess or conclude the game.

## Contributing
Contributions are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request.

## Credits
- This project was created by Hope Alemayehu.
- Quantum computing concepts and Grover's algorithm implementation based on Qiskit tutorials and documentation.

## Acknowledgements
Special thanks to the Qiskit development team for their work on open-source quantum computing tools and resources.

---
