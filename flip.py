#!/usr/bin/python3

from qiskit import *
import matplotlib.pyplot as plt
import random

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

plt.subplot(1,2,1)
z1,o1 = quantum(data)
quan = {"Heads":z1, "Tails":o1}
plt.bar(list(quan.keys()), quan.values(), width=0.25, align='edge')
plt.xlabel('Choice')
plt.ylabel('Probability')
plt.title('Probability of winning on Quantum Computer')

plt.subplot(1,2,2)
z2,o2= classical(data)
classic = {"Heads":z2, "Tails":o2}
plt.bar(list(classic.keys()), classic.values(), width=0.25, align='edge')
plt.xlabel('Choice')
plt.ylabel('Probability')
plt.title('Probability of winning on Classical Computer')

plt.show()
