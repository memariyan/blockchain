import hashlib
import json
from abc import ABC


class Block(ABC):

    def __init__(self, index: int, timestamp: str, data, nonce: int, previous_hash: str):
        self.index = index
        self.timestamp = timestamp
        self.nonce = nonce
        self.previous_hash = previous_hash
        self.data = data

    def hash(self) -> str:
        encoded_block = json.dumps(self.__dict__, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def proof_of_work(self, previous_block) -> int:
        return 0

    def check_proof_of_work(self, nonce: int, previous_block) -> bool:
        return False

    @staticmethod
    def from_dict(data: dict):
        tx = Block(
            sender=data["index"],
            receiver=data["timestamp"],
            amount=data["data"],
            amount=data["data"],
        )
        tx.id = data["id"]
        return tx
