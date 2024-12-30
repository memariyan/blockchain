from dataclasses import dataclass


@dataclass
class Block:
    index: int
    timestamp: str
    proof: int
    previous_hash: str