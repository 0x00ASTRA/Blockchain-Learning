# generate random transactions to use for testing chains

from hashlib import sha256
import json
import random
import keyboard

names = [
    'Tim',
    'Conner',
    'Ryan',
    'Michelle',
    'Amanda',
    'Kim',
    'Megan',
    'Kamala',
    'Peter',
    'Charlie',
]

def gen_rand_transaction():

    transfer_range_min, transfer_range_max  = -10000, 10000
    rand_name_index = random.randrange(len(names))
    rand_name = names[rand_name_index]
    rand_trans_number = random.randrange(transfer_range_min, transfer_range_max)
    transaction_type = ''

    if rand_trans_number == 0:
        transaction_type = 'null'

    elif rand_trans_number < 0:
        transaction_type = 'debit'

    else:
        transaction_type = 'credit'


    return json.dumps({'name': rand_name,
                       'type': transaction_type,
                       'amount': str(rand_trans_number).strip('-')})
"""
while True:
    try:
        if keyboard.is_pressed('g'):
            print(gen_rand_transaction())
            print(' ')

        if keyboard.is_pressed('q'):
            print('Exiting')
            break
    
    except:
        print('Key not recognized, hint: (g) - to load new transaction, (q) - to quit')
        break
"""

#print(gen_rand_transaction())
