import datetime
from urllib.parse import urlparse

import requests

from blockchain.types import Block


class Blockchain:
    def __init__(self):
        self.chains = []
        self.nodes = set()
        self.append(self.create_genesis_block())  # genesis block

    def create_genesis_block(self) -> Block:
        block = Block(
            index=len(self.chains) + 1,
            timestamp=str(datetime.datetime.now()),
            data=None,
            nonce=0,
            previous_hash='0', )
        return block

    def append(self, block: Block):
        self.chains.append(block)

    def get_previous_block(self) -> Block:
        return self.chains[-1]

    def is_chain_valid(self):
        return self._is_chain_valid(self.chains)

    @staticmethod
    def _is_chain_valid(chains):
        for index, block in enumerate(chains):
            if index == 0:
                continue

            previous_block = chains[index - 1]

            if block.previous_hash != previous_block.hash():
                return False
            if not block.check_proof_of_work(block.nonce, previous_block):
                return False

        return True

    def add_node(self, address: str):
        parsed_url = urlparse(address)
        self.nodes.add(parsed_url.netloc)

    def replace_chain(self) -> bool:
        network = self.nodes
        longest_chain = None
        max_length = len(self.chains)
        for node in network:
            response = requests.get(f'http://{node}/blockchain')
            response.raise_for_status()
            node_chain = response.json()['chain']
            chain_length = len(node_chain)
            if chain_length > max_length and self._is_chain_valid(node_chain):
                max_length = chain_length
                longest_chain = node

        if longest_chain :
            self.chains=longest_chain
            return True

        return False

blockchain = Blockchain()
