import datetime
import hashlib
from typing import List

from blockchain.block import Block
from cryptocurrency.types import Transaction


class MomoCoin(Block):

    def __init__(self, transactions : List[Transaction], previous_block: Block):
        data = [tx.to_dict() for tx in transactions]
        timestamp = str(datetime.datetime.now())
        nonce = self.proof_of_work(previous_block)
        previous_hash = previous_block.hash()
        super().__init__(previous_block.index + 1, timestamp, data, nonce, previous_hash)

    def transactions(self) -> List[Transaction]:
        return [Transaction.from_dict(tx) for tx in self.data]

    def proof_of_work(self, previous_block):
        nonce = 1
        while True:
            if self.check_proof_of_work(nonce, previous_block):
                return nonce

            nonce += 1

    def check_proof_of_work(self, nonce: int, previous_block: Block) -> bool:
        hash_operation = hashlib.sha256(str(nonce ** 2 - previous_block.nonce ** 2).encode()).hexdigest()
        return hash_operation[:4] == '0000'
