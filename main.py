import hashlib
import json
import datetime
from flask import Flask, jsonify
class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.pending_transactions = []
        self.new_block(previous_hash="This is a default hash.", proof=100)
    def new_block(self, proof, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp':  str(datetime.datetime.now()),
            'transactions': self.pending_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        self.pending_transactions = []
        self.chain.append(block)

        return block

    @property
    def last_block(self):
 
        return self.chain[-1]
    def new_transaction(self, sender, recipient, amount):
        transaction = {
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        }
        self.pending_transactions.append(transaction)
        return self.last_block['index'] + 1
    def proof_of_work(self, previous_proof):
        # miners proof submitted
        new_proof = 1
        # status of proof of work
        check_proof = False
        while check_proof is False:
            # problem and algorithm based off the previous proof and new proof
            hash_operation = hashlib.sha256(str(new_proof ** 2 - previous_proof ** 2).encode()).hexdigest()
            # check miners solution to problem, by using miners proof in cryptographic encryption
            # if miners proof results in 4 leading zero's in the hash operation, then:
            if hash_operation[:4] == '0000':
                check_proof = True
            else:
                # if miners solution is wrong, give mine another chance until correct
                new_proof += 1
        return new_proof
    def hash(self, block):
        string_object = json.dumps(block, sort_keys=True)
        block_string = string_object.encode()

        raw_hash = hashlib.sha256(block_string)
        hex_hash = raw_hash.hexdigest()
        return hex_hash
    def is_chain_valid(self, chain):
        # get the first block in the chain and it serves as the previous block
        previous_block = chain[0]
        # an index of the blocks in the chain for iteration
        block_index = 1
        while block_index < len(chain):
            # get the current block
            block = chain[block_index]
            # check if the current block link to previous block has is the same as the hash of the previous block
            if block["previous_hash"] != self.hash(previous_block):
                return False

            # get the previous proof from the previous block
            previous_proof = previous_block['proof']

            # get the current proof from the current block
            current_proof = block['proof']

            # run the proof data through the algorithm
            hash_operation = hashlib.sha256(str(current_proof ** 2 - previous_proof ** 2).encode()).hexdigest()
            # check if hash operation is invalid
            if hash_operation[:4] != '0000':
                return False
            # set the previous block to the current block after running validation on current block
            previous_block = block
            block_index += 1
        return True

blockchain = Blockchain()
t1 = blockchain.new_transaction("sahar", "shiva", '3 BTC')
t2 = blockchain.new_transaction("shiva", "mahdie", '2 BTC')
t3 = blockchain.new_transaction("mahdie", "leila", '1 BTC')
blockchain.new_block(12345)
t4 = blockchain.new_transaction("maryam", "parisa", '1 BTC')
t5 = blockchain.new_transaction("sara", "bahar", '0.5 BTC')
blockchain.new_block(6789)
print("Genesis block: ", blockchain.chain)

app = Flask(__name__)

'''@app.route('/mine_block', methods=['GET'])
def mine_block():
    # get the data we need to create a block
    previous_block = blockchain.last_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)

    block = blockchain.new_block(proof, previous_hash)
    response = {'message': 'Block mined!',
                'index': block['index'],
                'timestamp': block['timestamp'],
                'proof': block['proof'],
                'previous_hash': block['previous_hash']}
    return jsonify(response), 200'''


@app.route('/get_chain', methods=['GET'])
def get_chain():
    response = {'chain': blockchain.chain,
                'length': len(blockchain.chain)}
    return jsonify(response), 200


app.run(host='0.0.0.0', port=5000)
