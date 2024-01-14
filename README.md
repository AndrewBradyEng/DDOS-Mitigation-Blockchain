# DDOS Mitigation and Protection for Software Defined Networks
## Idea
The idea behind this project is to use blockchain style validation techniques in python to mitigate the risks of Direct Denial of Service attacks on Software Defined Networks by overloading the switch / controller bandwidth with packets.
The code should be ran in the linux terminal.

## ddos_simulation.py 
This script simulates a DDOS attack. Many packets are sent to a switch in the network to represent the direct denial of service attack.

## blockchain.py
This script simulates blockchain validation techniques. If a packet/s is sent from an unvalidated source in the network, the switch should reject this packet.
The technique attempted to be replicated is Proof of Authority (PoA).

## More
A full report of this project can be viewed in the "DDOS_Mitigation_Blockchain_SDN.pdf" file in the main repository.
