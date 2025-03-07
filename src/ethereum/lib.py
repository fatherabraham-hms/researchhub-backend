from decimal import Decimal

from web3 import Web3

from ethereum.utils import decimal_to_token_amount
from researchhub import settings
from researchhub.settings import w3
from utils.aws import create_client

TOKENS = {
    "RSC": {
        "name": "ResearchCoin",
        "contract_address": settings.WEB3_RSC_ADDRESS,
        "ticker": "RSC",
        "denomination": 18,
        "reputation_exchange_rate": "1.0",
    },
}

RSC_CONTRACT_ADDRESS = TOKENS["RSC"]["contract_address"]  # convenient


def get_token_address_choices():
    return [
        (token["contract_address"], f'{token["name"]} address')
        for token in TOKENS.values()
    ]


TOKEN_ADDRESS_CHOICES = get_token_address_choices()


def convert_reputation_amount_to_token_amount(token, reputation_amount):
    """Converts `reputation_amount` based on the `token` reputation exchange
    rate.

    Returns:
        (int, str) -- Amount of `token` in integer and decimal forms.
    """

    if reputation_amount < 0:
        raise ValueError("`reputation_amount` must be a positive number")

    token = TOKENS[token]
    rate = Decimal(str(token["reputation_exchange_rate"]))
    reputation = Decimal(str(reputation_amount))
    total = rate * reputation
    denomination = token["denomination"]
    return decimal_to_token_amount(total, denomination), str(total)


def get_nonce(w3, account):
    return w3.eth.get_transaction_count(account)


def get_gas_estimate(method_call):
    return 120000


def get_eth_balance(w3, account):
    return w3.eth.get_balance(account)


def get_fee_estimate(w3, method_call):
    """Returns fee estimate for `method_call` in wei based on estimateGas and
    generateGasPrice.
    """
    gas_estimate = get_gas_estimate(method_call)
    gas_price = w3.eth.generate_gas_price()  # wei
    return gas_estimate * gas_price


def execute_erc20_transfer(w3, sender, sender_signing_key, contract, to, amount):
    """Sends `amount` of the token located at `contract` to `to`.

    !!! NOTE: This method should be used carefully because it sends funds.

    Returns the transaction hash.

    Args:
        contract (obj) - w3 contract instance of the ERC20
        to (str) - Ethereum address of recipient
        amount (int) - Amount of token to send (in smallest possible
            denomination)
    """
    decimals = contract.functions.decimals().call()
    decimal_amount = amount * 10 ** int(decimals)
    return transact(
        w3, contract.functions.transfer(to, decimal_amount), sender, sender_signing_key
    )


def transact(w3, method_call, sender, sender_signing_key, gas=None):
    """Executes the contract's `method_call` on chain.

    !!! NOTE: This method should be used carefully because it sends funds.

    Args:
        gas (int) - Amount of gas to fund transaction execution. Defaults to
            method_call.estimateGas()
        sender (str) - Address of message sender
        sender_signing_key (bytes) - Private key of sender
    """
    gas_estimate = get_gas_estimate(method_call)
    checksum_sender = Web3.to_checksum_address(sender)
    tx = method_call.build_transaction(
        {
            "from": checksum_sender,
            "nonce": get_nonce(w3, checksum_sender),
            "gas": gas or gas_estimate,
        }
    )
    signing_key = sender_signing_key
    signed = w3.eth.account.sign_transaction(tx, signing_key)
    tx_hash = w3.eth.send_raw_transaction(signed.rawTransaction)
    return tx_hash.hex()


def get_private_key():
    s3_client = create_client("s3")
    response = s3_client.get_object(
        Bucket=settings.WEB3_KEYSTORE_BUCKET,
        Key=settings.WEB3_KEYSTORE_FILE,
    )
    encrypted_key = response["Body"].read().decode("utf-8")

    if settings.WEB3_KEYSTORE_PASSWORD:
        return w3.eth.account.decrypt(encrypted_key, settings.WEB3_KEYSTORE_PASSWORD)
    else:
        return encrypted_key
