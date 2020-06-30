'''
This is a simple challenge introducing to the some of the 
concepts related to gates in Quantum Circuits and explains about
the concept of superposition

You are playing a game with 2 computers 
A classical one and a Quantum one
The computer shows you heads initially
It then performs an operation on it(Choosing heads or tails)
Now you have to perform an operation on the coin(Choose heads or tails)
The computer performs another operation on it(Choosing heads or tails)

It then shows you the output
If Heads is the output, you lose
If Tails is the output you win

These operations are performed on two computers,
Quantum and Classical. Find your chances to win

This code is inspired from the TED Talk
https://www.ted.com/talks/shohini_ghose_a_beginner_s_guide_to_quantum_computing

Codes which helped us
https://github.com/MackEdweise/TEDCoinToss
https://github.com/qiskit-community/qiskit-community-tutorials/blob/master/games/Quantum-Coin-Game.ipynb
'''

#!/usr/bin/python3

from qiskit import *
import matplotlib.pyplot as plt
import random
import csv

simulator = Aer.get_backend('qasm_simulator')
# Process in which this must happen
# Computer's turn
# Human Response
# Computer's turn

#Helper Function
def measure(inp):
    circuit = QuantumCircuit(1,1)
    #Check this if there are any issues
    circuit.measure(0,0)
    val = inp + circuit
    return val

'''
Choices
Heads = Identity gate(since heads means keeping in same position)
Tails = Pauli X gate(since tails means switching the position)
Superposition of H&T = Hadamard Gate(Since H-Gate means a superposition)
'''
def quantum(inp):
    count_0 = 0
    count_1 = 0

    for i in inp:
        circuit = QuantumCircuit(1)

        # Hadamard Gate applied since a qubit in a
        # quantum computer is superposition b/w 0 and 1
        circuit.h(0)

        #Checking User input
        if(i==0):
            circuit.iden(0)
        elif(i==1):
            circuit.x(0)

        # Hadamard Applied again since choice by a 
        # quantum computer is superposition b/w 0 and 1
        circuit.h(0)

        val = measure(circuit)

        #Generates a simulation instead of working it on quantum machine
        simulation = execute(val, simulator, shots=200)
        result = simulation.result()
        count = result.get_counts(val)
        if("0" in count):
            count_0+=1
        elif("1" in count):
            count_1+=1
    
    p_0 = (count_0)/(count_0+count_1)
    p_1 = (count_1)/(count_0+count_1)

    return p_0, p_1


def classical(inp):
    count_0 = 0
    count_1 = 0

    for i in inp:
        circuit = QuantumCircuit(1)
        
        #Classic Comp turn Either 0 or 1
        #Since it can decide b/w them
        comp_c = random.randint(0,1)
        if(comp_c==0):
            circuit.iden(0)
        elif(comp_c==1):
            circuit.x(0)
        
        #User turn
        if(i==0):
            circuit.iden(0)
        elif(i==1):
            circuit.x(0)

        #Classical comp turn
        comp_c = random.randint(0,1)
        if(comp_c==0):
            circuit.iden(0)
        elif(comp_c==1):
            circuit.x(0)

        val = measure(circuit)

        #Generates a simulation instead of working it on quantum machine
        simulation = execute(val, simulator, shots=200)
        result = simulation.result()
        count = result.get_counts(val)

        if("0" in count):
            count_0+=1
        elif("1" in count):
            count_1+=1
    
    p_0 = (count_0)/(count_0+count_1)
    p_1 = (count_1)/(count_0+count_1)

    return p_0, p_1

with open("inputs.csv") as ip:
    data = (ip.read().split('\n'))

data.remove('')

plt.figure()

plt.subplot(2,1,1)
z1,o1 = quantum(data)
quan = {"Heads":z1, "Tails":o1}
plt.bar(list(quan.keys()), quan.values())
plt.xlabel('Choice')
plt.ylabel('Probability')
plt.title('Probability of winning on Quantum Computer')

plt.subplot(2,1,2)
z2,o2= classical(data)
classic = {"Heads":z2, "Tails":o2}
plt.bar(list(classic.keys()), classic.values())
plt.xlabel('Choice')
plt.ylabel('Probability')
plt.title('Probability of winning on Classical Computer')

plt.show()