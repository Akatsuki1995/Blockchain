from brownie import MoneyCollectible, accounts, network, config
from scripts.helpful_scripts import fund_money_collectible


def main():
    dev = accounts.add(config["wallets"]["from_key"])
    print(network.show_active())
    # publish_source = True if os.getenv("ETHERSCAN_TOKEN") else False # Currently having an issue with this
    publish_source = False
    money_collectible = MoneyCollectible.deploy(
        config["networks"][network.show_active()]["vrf_coordinator"],
        config["networks"][network.show_active()]["link_token"],
        config["networks"][network.show_active()]["keyhash"],
        {"from": dev},
        publish_source=publish_source,
    )
    fund_money_collectible(money_collectible.address)
    return money_collectible