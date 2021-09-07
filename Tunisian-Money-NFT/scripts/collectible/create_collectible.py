from brownie import MoneyCollectible, accounts, config
from scripts.helpful_scripts import get_value, fund_money_collectible
import time

def main():
    dev = accounts.add(config["wallets"]["from_key"])
    money_collectible = MoneyCollectible[len(MoneyCollectible) - 1]
    fund_money_collectible(money_collectible.address)
    transaction = money_collectible.createCollectible("None", {"from": dev})
    print("Waiting on second transaction...")
    # wait for the 2nd transaction
    transaction.wait(1)
    requestId = transaction.events["requestedCollectible"]["requestId"]
    print(requestId)
    token_id = money_collectible.requestIdToTokenId(requestId)
    time.sleep(55)
    value = get_value(money_collectible.tokenIdToValue(token_id))
    print("Money value of tokenId {} is {}".format(token_id, value))