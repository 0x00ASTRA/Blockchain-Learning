import  os
import blockchain
from flask import Flask, render_template
import json
import gen_transactions as gt
import datetime
from time import sleep

app = Flask(__name__)

chain1 = blockchain.Blockchain(difficulty=2)

def mine_block():
    print('Mining Block...')
    start_time = datetime.datetime.now()
    answer = False
    while answer == False:
        answer = chain1.mine()
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

def log_chain():
    with open("json/chain.json", "w") as f:
        f.writelines(get_chain())

@app.route('/api', methods=['GET'])

def get_data():
    print(get_chain())
    return get_chain()

print('here')
# for 10 blocks do this

def add_and_mine():
    # for _ in range(5): 
    #         chain1.add_new_transaction(gt.gen_rand_transaction())
    if mine_block() == False:
        try:
            print("adding 5 transactions...")    
            for _ in range(5):
                chain1.add_new_transaction(gt.gen_rand_transaction())
            
            print("transactions added.")

        except:
            print("error adding transactions")
        print("uncomf trans: " + str(chain1.unconfirmed_transactions))


print("Executing Chain Creation...")
for i in range(1,11):
    pr = os.fork()
    if pr is 0:
        print(" ")
        add_and_mine()
    else:    
        print("The parent process is now waiting")
        cpe = os.wait()
        print("Child process with number %d exited" % (cpe[0]))
        print("Parent process with number %d exiting after child has executed its process" % (os.getpid()))
        print("The parent process is", (os.getpid()))

    if not cpe:
        print(f"{i} complete")

for i in range(1,11):
    add_and_mine()
    print(f"{i} complete")

get_data()
log_chain()

@app.route('/', methods=['GET'])
def mainpage():
    return  render_template('mainpage.html')
# main = app.run(debug=True, port=7000)
app.run(debug=True, port=7000)
    
    

 