## Bitcoin Testnet Wallet - In-Progress, Not A Production Wallet
This is a Bitcoin testnet wallet which can: generate new addresses each time you want to recieve a transaction, synchronize your UTXOs, and constructs raw hex p2pkh transactions which you can broadcast here: https://blockstream.info/testnet/tx/push . 
This wallet utilizes the Bitcoin library from [Programming Bitcoin](https://www.oreilly.com/library/view/programming-bitcoin/9781492031482/) by Jimmy Song, licensed under [CC-BY-NC-ND](https://creativecommons.org/licenses/by-nc-nd/4.0/legalcode), and published by [O'Reilly Media, Inc.March 2019](https://learning.oreilly.com/library/publisher/oreilly-media-inc/). 

##Running The Testnet Wallet
The wallet is designed so that the block_syncer() function in block_logger.py is always running, always looking for UTXOs which can be spent by your numerous addresses and adding them to the respective user's UTXO file. With block_syncer() running in the background, you can run interface.py to interact with the wallet. It should also be noted that interface.py can be run independently, but your UTXOs won't be continously updated.
