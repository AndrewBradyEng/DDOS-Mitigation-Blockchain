from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSSwitch, RemoteController

class PoATopology(Topo):
    def build(self):
        # Create switches
        switch1 = self.addSwitch('s1')

        # Create validators
        validator1 = self.addHost('validator1')
        validator2 = self.addHost('validator2')
        validator3 = self.addHost('validator3')

        # Create unvalidated host
        unvalidated_host = self.addHost('unvalidated_host')

        # Connect nodes to the switch
        self.addLink(validator1, switch1)
        self.addLink(validator2, switch1)
        self.addLink(validator3, switch1)
        self.addLink(unvalidated_host, switch1)

        # Assign IP addresses manually
        self.addLink(validator1, switch1, intfName1='veth1', params1={'ip': '10.0.0.1/24'})
        self.addLink(validator2, switch1, intfName1='veth2', params1={'ip': '10.0.0.2/24'})
        self.addLink(validator3, switch1, intfName1='veth3', params1={'ip': '10.0.0.3/24'})
        self.addLink(unvalidated_host, switch1, intfName1='veth4', params1={'ip': '10.0.0.4/24'})

def simulate_poa():
    net = Mininet(topo=PoATopology(), switch=OVSSwitch, controller=RemoteController)
    net.start()

    # List of validators
    validators = ['validator1', 'validator2', 'validator3']
    current_validator = 0  # Index to keep track of the current validator proposing the block
    blockchain = []  # Store blocks in the blockchain

    # Simulate PoA consensus logic (simple round-robin)
    for round_number in range(1, 11):  # Simulating 10 rounds of block proposal
        current_validator = (current_validator + 1) % len(validators)  # Move to the next validator
        proposing_validator = validators[current_validator]
        print(f"Round {round_number}: Validator {proposing_validator} proposes a new block")

        # Simulate message passing between validators
        for validator in validators:
            if validator != proposing_validator:
                if validator == 'unvalidated_host':
                    # Simulate an unvalidated host attempting to send a message
                    print(f"Unauthorized message attempted from unvalidated host to Validator {validator} - Message dropped.")
                else:
                    print(f"Validator {proposing_validator} sends a message to Validator {validator}")

        # Simulate block creation (adding to blockchain)
        new_block = {
            'validator': proposing_validator,
            'transactions': [f"Transaction {round_number}-{i}" for i in range(3)]  # Simulating 3 transactions per block
        }
        blockchain.append(new_block)

    # Display the blockchain
    print("\nBlockchain:")
    for block in blockchain:
        print(block)

    net.stop()

if __name__ == "__main__":
    simulate_poa()
