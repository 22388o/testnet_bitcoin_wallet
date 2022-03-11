from multiprocessing import Process

from jbok import get_tpub, get_tprv
from user_manager import make_user, user_login, has_login
from send_to_storage import send_to_storage, get_all_balance
from stx import get_balance, multi_send
from rtx import recieve_tx
from block_logger import block_syncer
from block_utils import is_synched, get_known_height 

def run_wallet(p):
    print("NOTE: this wallet only operates on the testnet, enter 'sign out' to log into a different account and 'quit' to exit.")

    username = has_login()
    print("I can: calculate your current balance[cb], send transactions[stx], recieve transactions[rtx], check if your wallet is fully synchronized with the blockchain[status], change the full node you get information from[change node] and get your extended public key [tpub] or your extended private key[tprv]")
    p.start()

    active = True
    while active:
        print("What can I help you with?")
        option = input("You: ")
        if option == "stx":
            if is_synched():
                multi_send(username)
            else:
                print("Your wallet is currently in the process of synching with the blockchain. Please try again later.")
        elif option == "rtx":
            recieve_tx(username)
        elif option == "cb":
            if is_synched() == False:
                print("Please note that your wallet is still in the process of synching with the blockchain.")
            balance = get_balance(username, unconfirmed=True)
            print(f"Your current balance is: {balance[0]} Satoshis")
            if balance[1] != 0:
                print(f"You also have an additional unconfirmed balance of {balance[1]} Satoshis")
        elif option == "quit":
            active = False
        elif option == "sign out":
            username = has_login()
        elif option == "tpub":
            print(get_tpub(username))
        elif option == "tprv":
            print(get_tprv(username))
        elif option == "change node":
            new_host = input("New node: ")
            with open("network_settings.py", 'w') as net_file:
                net_file.write(f'HOST = "{new_host}"')
            print("Please restart your wallet for these changes to take full affect everywhere")
        elif option == "storage":
            if get_all_balance() == 0:
                print("You have 0 testnet bitcoin")
            else:
                if is_synched():
                    send_to_storage()
                else:
                    print("Your wallet is currently in the process of synching with the blockchain. Please try again later.")
        elif option == "status":
            if is_synched():
                print("The wallet is fully synchronized with the blockchain")
            else:
                print("The wallet is in the process of synchronizing with the blockchain.")
            print(f"The latest known block height is: {get_known_height()}")

if __name__ == '__main__':
    
    p = Process(target=block_syncer)
    run_wallet(p)
    p.terminate()