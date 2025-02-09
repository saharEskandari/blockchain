# Blockchain Implementation in Python

This is a simple blockchain implementation using Python and Flask. It includes basic features such as adding transactions, mining new blocks, and retrieving the blockchain.

## Features
- Create a new blockchain with a genesis block.
- Add new transactions.
- Mine new blocks using Proof of Work (PoW).
- Verify the integrity of the blockchain.
- Expose a REST API to retrieve the blockchain.

## Technologies Used
- Python
- Flask
- hashlib
- JSON
- datetime

## Installation
 Install dependencies:
   ```bash
   pip install flask
   ```

## Usage


### API Endpoints
- **Get the blockchain:**
  ```bash
  curl http://127.0.0.1:5000/get_chain
  ```
  **Response:**
  ```json
  {
    "chain": [...],
    "length": 2
  }
  ```

### Example Transactions
You can manually add transactions using the `new_transaction` method in the code before mining a block.

### Mining Blocks
There is a commented-out `/mine_block` endpoint in the code. Uncomment it and restart the server to enable mining new blocks.

## Future Improvements
- Implement a peer-to-peer network for decentralized blockchain.
- Add transaction verification.
- Improve mining efficiency.

## License
This project is licensed under the MIT License.

