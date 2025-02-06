# PolicyReporterOA
## Objective
The goal is to take a string of ones and zeroes representing an unsigned binary integer and return the remainder when divided by 3. Instead of converting the string to an integer type and using modulus, a finite state machine (FSM) will be used instead.

### FSM

The FSM takes in characters from the input string, starting at the most significant bit and transitions between the states S0, S1, S2 depending on the character. The remainder returned by the FSM is determined by the final state after all characters have been processed.

<img width="685" alt="image" src="https://github.com/user-attachments/assets/4b1cc72b-05c3-4535-bb9f-7912b45c710b" />

The table below indicates the remainder returned for each state.
<img width="351" alt="image" src="https://github.com/user-attachments/assets/a811b58f-5583-4095-b73c-0bee5aab6cc8" />


### Example
For the input string "010" (binary representation of 2", the machine will operate as follows:
<img width="317" alt="image" src="https://github.com/user-attachments/assets/a03395d2-b676-43c6-9608-abd17876c0ee" />

Since the final state is S2, the remainder will be 2.

## Running the Program
- Before attempting to run any commands in the terminal, please install the latest version of python on your device. The download link can be found [here](https://www.python.org/downloads/)
- To start the program, ensure you are in the **root folder** and run the following command in the terminal:

```
python3 -m src.main
```
  
- Once the program has started, you will be prompted to enter a string of ones and zeroes.  Any input containing special characters, white spaces or numbers that are not 1 or 0 will not be accepted.
- Upon pressing enter, the remainder will be printed in the terminal.
- To exit the program, enter "exit".
  
## Running Tests
- Individual tests suites for validating remainders, classes and the input validator can be found in   the tests folder.
- To run invidual test suites, ensure you are in the **root folder** and run the following command in the terminal:
```
python3 -m unittest tests.<test_file_name>
```
- NOTE: Do not include the ".py" extension in the file name.
---
- To run all test suites, ensure you are in the **root folder** and run the following command in the terminal:
```
python3 run_tests.py
```
