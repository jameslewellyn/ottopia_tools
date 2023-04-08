#!/usr/bin/env python3
"""Contains the main package functionality."""
import logging
import json
from web3 import Web3

logging.basicConfig(level=logging.INFO)

# The address of the account to check the balance for
account_address = "0xa6c4F123b99eaF51E63dD31497f4921aD6761230"

# The address of the Matic token contract on the Matic network
matic_token_address = "0x6e8A9Cb6B1E73e9fCe3FD3c68b5af9728F708eB7"

# The decimal places of the Matic token (18 decimal places for most tokens)
matic_token_decimal_places = 18

# Load the Matic token contract ABI
with open("otter1.json", "r") as f:
    matic_token_abi = json.load(f)


def main() -> None:
    """Do the main thing."""
    # Get arguments
    w3 = Web3(Web3.HTTPProvider("https://polygon-mainnet.infura.io/v3/0d6112d636444d5ebce0eeedb8fd1f6d"))
    # num: int = w3.eth.get_balance("0xa6c4F123b99eaF51E63dD31497f4921aD6761230")
    matic_token_contract = w3.eth.contract(address=matic_token_address, abi=matic_token_abi)
    balance = matic_token_contract.functions.balanceOf(account_address).call()
    balance_in_matic_tokens = balance / (10**matic_token_decimal_places)

    logging.info(f"{balance = }")
