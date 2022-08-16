# define what a block is:
# 
# a block is a immutable verified state in timeline.
import datetime
import hashlib
import json

class Block:
    def __init__(self, index, timestamp, prev_hash, nonce=0, transactions=[]):
         # define the structure of our block
        self.index = index
        self.timestamp = timestamp
        self.prev_hash = prev_hash
        self.nonce = nonce
        self.transactions = transactions
    
    def calculate_hash(self):
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()


class Blockchain:
    def __init__(self, difficulty):
        self.unconfirmed_transactions = []
        self.chain = []
        self.create_genesis_block()
        self.difficulty = difficulty

    def create_genesis_block(self):
        genesis_block = Block(index=0, timestamp=str(datetime.datetime.now()), prev_hash='0000000000000000000000000000000000000000000000000000000000000000')
        genesis_block.hash = genesis_block.calculate_hash()
        self.chain.append(genesis_block)

    @property
    def last_block(self):
        return self.chain[-1]

    def proof_of_work(self, block):
        print("difficulty: " + str(self.difficulty))
        block.nonce = 0
        calculated_hash = block.calculate_hash()
        while not calculated_hash.startswith('0' * self.difficulty):
            block.nonce += 1
            calculated_hash = block.calculate_hash()

        print("Nonce: " + str(block.nonce))
        return calculated_hash

    def add_block(self, block, proof):
        prev_hash = self.last_block.hash
        if prev_hash != block.prev_hash:
            return False
        if not self.is_valid_proof(block, proof):
            return False
        block.hash = proof
        self.chain.append(block)
        self.difficulty += 1
        return True

    def is_valid_proof(self, block, block_hash):
        return (block_hash.startswith('0' * self.difficulty) and block_hash == block.calculate_hash())

    def add_new_transaction(self, transaction):
        self.unconfirmed_transactions.append(transaction)

    def mine(self):
        if not self.unconfirmed_transactions:
            print("false")
            return False

        last_block = self.last_block

        new_block = Block(index=last_block.index + 1,
                          transactions=self.unconfirmed_transactions,
                          prev_hash=last_block.hash, timestamp=str(datetime.datetime.now))

        proof = self.proof_of_work(new_block)
        self.add_block(new_block, proof)
       
        self.unconfirmed_transactions = []
        return new_block.index 
