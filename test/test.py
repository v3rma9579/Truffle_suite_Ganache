from web3 import Web3,HTTPProvider
import json
def connect_with_blockchain():

    web3=Web3(HTTPProvider('HTTP://127.0.0.1:7545'))
    web3.eth.defaultAccount=web3.eth.accounts[0]

    with open(r"build\contracts\Reverse.json") as f:
        artifact_json=json.load(f)
        contract_abi=artifact_json['abi']
        contract_address=artifact_json['networks']['5777']['address']
        contract=web3.eth.contract(abi=contract_abi,address=contract_address)

    return(contract,web3)


contract,web3=connect_with_blockchain()
tx_hash=contract.functions.reverseDigits(67877).transact()
web3.eth.waitForTransactionReceipt(tx_hash)
result =contract.functions.getResult().call()

print(result)






