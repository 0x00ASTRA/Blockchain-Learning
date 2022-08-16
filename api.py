import blockchain
from flask import Flask, request
import requests
import json
import gen_transactions as gt
import datetime
from time import sleep

app = Flask(__name__)

chain1 = blockchain.Blockchain(difficulty=2)

def mine_block():
    print('mining...')
    start_time = datetime.datetime.now()
    answer = False
    while answer != True:
        answer = chain1.mine() == True
        return answer
        
    end_time = datetime.datetime.now()
    mined = json.dumps({'mined': answer,
                        'start': str(start_time),
                        'end': str(end_time),
                        'exec-time': str(end_time - start_time)})
    print(mined)
    return f'<h1>{mined}</h1>'

def get_chain():
    chain_data = []
    for block in chain1.chain:
        chain_data.append(block.__dict__)
    return json.dumps({'length': len(chain_data),
                       'chain': chain_data})

@app.route('/', methods=['GET'])

def get_data():
    return get_chain()

print('here')
# for 10 blocks do this

def add_and_mine():
    for _ in range(5): 
            chain1.add_new_transaction(gt.gen_rand_transaction())

    if mine_block() != True:
        try:    
            for _ in range(5):
                chain1.add_new_transaction(gt.gen_rand_transaction())
                print("transaction added")
        except:
            print("error")
for i in range(1,10):
    add_and_mine()
    print(f"{i} complete")

# main = app.run(debug=True, port=7000)
app.run(debug=True, port=7000)
    
    

 