from brownie import MoneyCollectible
from scripts.helpful_scripts import fund_money_collectible


def main():
    money_collectible = MoneyCollectible[len(MoneyCollectible) - 1]
    fund_money_collectible(money_collectible)
