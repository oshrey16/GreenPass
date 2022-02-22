import json
# from web3 import Web3
# from eth_account import Account
from datetime import timedelta, datetime
from web3 import Web3


infura_url = 'https://ropsten.infura.io/v3/d4cc9700040444069b45a42f154e1685'
web3 = Web3(Web3.HTTPProvider(infura_url))

# epoch_day = 86400
print("Connection: " + str(web3.isConnected()))
# First
abi = json.load(open('abi.json','r'))
# abi = json.load(f)
address = web3.toChecksumAddress(0x67b762869f742d84d817e9053552b1ecc584d4e7)
# Owner #
web3.eth.defaultAccount = '0x3F085894effe704c13BFBF2bE30e45bD440c6B20'

contract = web3.eth.contract(address=address, abi=abi)

# print(web3.eth.get_balance('0x3F085894effe704c13BFBF2bE30e45bD440c6B20'))
print(contract)

print("Owner: " + str(contract.functions.isOwner().call()))
privatekey = 0xb9b1d971de4c08f7f521ae1350d096e8d958ca3e7e706cb1eb7d6a97d3bc7a03
print("Count of GreenPass: " + str(contract.functions.count().call()))
# print(web3.eth.accounts)
# f = web3.eth.accounts.create()
# print(f)
count = contract.functions.count().call()

def get_all_greenpass():
    global count
    count = contract.functions.count().call()
    result = []
    for i in range(count):
        index = contract.functions.indexes(i+1).call()
        greenpass = get_single_greenpass(index)
        result.append(greenpass)
        print(f'Green Pass #{i+1}:\n\t'
              f'Name:\t\t{result[i][0]}\n\t'
              f'ID:\t\t\t{result[i][1]}\n\t'
              f'Expires:\t{result[i][2]}')
    print('RESULT = ' + str(result))
    return result


def get_single_greenpass(id):
    greenpass = contract.functions.passs(id).call()
    name = f'{greenpass[0]} {greenpass[1]}'
    # print('Getting ID')
    id = greenpass[2]
    # print('Getting expiration')
    expiration = datetime.fromtimestamp(greenpass[3]).strftime("%d-%m-%Y")
    return [name, id, expiration]


def add_green_pass(first_name, last_name, id, expiration):
    r= contract.functions.addGreenPass(first_name, last_name, id, expiration).buildTransaction()
    r.update({ 'nonce' : web3.eth.get_transaction_count(web3.eth.defaultAccount) })
    signed_tx = web3.eth.account.sign_transaction(r, 0xb9b1d971de4c08f7f521ae1350d096e8d958ca3e7e706cb1eb7d6a97d3bc7a03)
    txn_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    txn_receipt = web3.eth.wait_for_transaction_receipt(txn_hash)
    print("Count of GreenPass: " + str(contract.functions.count().call()))


def renew_green_pass(id):
    greenpass = contract.functions.passs(id).call()
    exp = int(greenpass[3])
    print(exp)
    r= contract.functions.updateExpiration(id,exp).buildTransaction()
    r.update({ 'nonce' : web3.eth.get_transaction_count(web3.eth.defaultAccount) })
    signed_tx = web3.eth.account.sign_transaction(r, 0xb9b1d971de4c08f7f521ae1350d096e8d958ca3e7e706cb1eb7d6a97d3bc7a03)
    txn_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    txn_receipt = web3.eth.wait_for_transaction_receipt(txn_hash)
    print("Count of GreenPass: " + str(contract.functions.count().call()))