# qc-coinflip
A simple coin-flipping game to checking the winning probabilities on Quantum Computer and Classical Computer

### Understanding qubits and gates using a small coin flipping experiment

Once we understood what Qubits are, we wanted to practically try it out on a quantum computer to check how the concept of superposition works. For this we used Qiskit, which is a python framework which simulates the results by a quantum computer. Alternatively we could have used IBM Quantum Experience for running the code on actual Quantum Computer like Melbourne, but we instead chose to stick to the simulation. The code for this experiment can be accessed here. 

This is a simple coin flipping simulator. The game goes as follows. You have a fair and unbiased coin. You have a computer playing against you. Initially assume that the coin is in Heads position. The computer first chooses to either turn the coin or leave it as is. Note that all the moves are hidden, ie. a computer doesn't know what human did and human doesn't know what human did. The second turn would be yours. You may also now turn the coin or leave it as it is. Computer then plays the final move, where it can choose to flip the coin or leave it as it is. After these three steps the final position of coin is revealed. If Heads is the face, computer wins, else Player wins.

We sent out a form asking our batch-mates to play this, and this was the result.

We had 2 different opponents, one was a classical computer and other was a quantum computer. If the player played against a classical computer he/she had an approximate 50-50 chance to win the game. But, if we played this on the Quantum Computer, the player loses in almost all the cases. Even if there are a few cases, it might occur due to some noise, but since we are using a Theoretical Simulator here, we might not be bound to such errors. In order to see this errors, you can alternatively check this on IBM Quantum Experience.

What does this experiment teach us? The basic analogies in the experiment are as follows, the coin is a register. And it has a place to be filled in with, either a bit or a qubit, which depends on the computer the player is playing against. A bit here is a head or a tail, where 0 represents head and 1 represents tail. In a classical computer, it is certain that the bit will be either 0 or 1 but not both, hence there is a 50-50 chance to win. So if a player chooses to keep it as Heads, Identity gate is applied, if he/she chooses to flip it to Tails, a Pauli-X gate is applied. But when we look at the quantum computer, the qubit can exist in superposition of both Heads and Tails, so a new gate needs to be introduced to identify this state. It is the Hadamard gate. 

A quantum gate acting on a single qubit can be defined by its action on the basis vectors *|0*⟩ *and |1*⟩. 

*Identity gate* maps |0⟩ to |0⟩ and |1⟩ to |1⟩

*X-Gate* maps |0⟩ to |1⟩ and |1⟩ and |0⟩

*Hadamard-Gate* maps |0⟩ to |0⟩+|1⟩/√2 and |1⟩ to |0⟩-|1⟩/√2

So now we have 2 cases. 

1) If player chooses not to flip the coin 

2) If player chooses to flip the coin

**Case 1**

Firstly, Hadamard gate is applied on initial |0⟩ state which gives, |0⟩+|1⟩/√2. Now we apply the user's choice to use Identity gate. It will return the same output. Now apply Hadamard gate on this output as it is the computer's choice and it will be in superposition. Hence H(|0⟩+|1⟩/√2), will return |0⟩ on calculations, which is Heads.

**Case 2**

Firstly, Hadamard gate is applied on initial |0⟩ state which gives, |0⟩+|1⟩/√2. Now we apply the user's choice to use Pauli-X gate. It will return the same output since X(|0⟩+|1⟩/√2) = |1⟩+|0⟩/√2. Now apply Hadamard gate on this output as it is in superposition. Hence  H(|1⟩+|0⟩/√2), will return |0⟩ on calculations, which is Heads.

Hence due to the principle of superposition, it is always a Heads as an output.
