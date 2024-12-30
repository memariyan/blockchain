import datetime
import hashlib
import json

from blockchain.types import Block


class Blockchain:
    def __init__(self):
        self.chains = []
        self.create_block(proof=0, previous_hash='0')  # genesis block

    def create_block(self, proof, previous_hash) -> Block:
        block = Block(
            index=len(self.chains) + 1,
            timestamp=str(datetime.datetime.now()),
            proof=proof,
            previous_hash=previous_hash, )

        self.chains.append(block)
        return block


    def get_previous_block(self) -> Block:
        return self.chains[-1]

    def proof_of_work(self, previous_proof) -> int:
        new_proof = 1
        while True:
            if self.check_proof_of_work(previous_proof, new_proof):
                return new_proof

            new_proof += 1

    @staticmethod
    def check_proof_of_work(previous_proof, new_proof) -> bool:
        hash_operation = hashlib.sha256(str(new_proof ** 2 - previous_proof ** 2).encode()).hexdigest()
        return hash_operation[:4] == '0000'

    @staticmethod
    def hash(block: Block) -> str:
        encoded_block = json.dumps(block.__dict__, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def is_chain_valid(self):
        for index, block in enumerate(self.chains):
            if index == 0:
                continue

            previous_block = self.chains[index - 1]

            if block.previous_hash != self.hash(previous_block):
                return False
            if not self.check_proof_of_work(previous_block.proof, block.proof):
                return False

        return True
