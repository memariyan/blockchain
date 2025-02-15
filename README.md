## Overview
This project implements a simple blockchain infrastructure and a cryptocurrency that operates on top of it. The blockchain ensures secure, decentralized, and immutable transactions, while the cryptocurrency layer provides a means of exchange.

## Features
- **Blockchain Implementation**: A simple yet functional blockchain with proof-of-work (PoW) consensus.
- **Cryptocurrency Layer**: A digital currency operating on the blockchain.
- **Transaction Handling**: Users can create and broadcast transactions.
- **Mining Functionality**: Nodes can mine blocks and earn rewards.
- **Peer-to-Peer Network**: A distributed system allowing nodes to synchronize blockchain data.
- **REST API**: Provides interaction with the blockchain through HTTP requests.

## Installation
### Prerequisites
Ensure you have Python installed (recommended version: 3.8 or higher).

### Clone the Repository
```bash
git clone https://github.com/memariyan/blockchain.git
cd blockchain
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

## Usage
### Start a Node
Run the blockchain node server:
```bash
python blockchain.py
```

### Creating a New Transaction
Use the API to create transactions:
```bash
curl -X POST http://localhost:8000/api/blockchain/momo/transaction -H "Content-Type: application/json" -d '{"sender": "kk"}'
```

### Mining a Block
```bash
curl -X POST http://localhost:8000/api/blockchain/momo/mine
```

### Checking the Blockchain
```bash
curl -X GET http://localhost:8000/api/blockchain
```

### Connecting Nodes
```bash
curl -X POST http://localhost:8000/api/blockchain/nodes/connect -H "Content-Type: application/json" -d '{"nodes": ["http://127.0.0.1:8000"]}'
```

### Checking Blockchain Validity
```bash
curl -X GET http://localhost:8000/api/blockchain/check
```
