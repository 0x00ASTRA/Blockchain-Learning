import hashlib
import json

file = open("block1.json",  "r")
block_string = json.load(file)

def calculate():
    print(hashlib.sha256().hexdigest())

calculate()