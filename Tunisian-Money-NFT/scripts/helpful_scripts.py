from brownie import ( network, accounts, config, interface)

def fund_money_collectible(nft_contract):
    dev = accounts.add(config['wallets']['from_key'])
    link_token = interface.LinkTokenInterface(
        config['networks'][network.show_active()]['link_token'])
    link_token.transfer(nft_contract, 1000000000000000000, {"from": dev})
def get_value(value_number):
    switch = {0: "FIFTY", 1:"ONE_HUNDRED", 2: "ONE_THOUSAND", 3: "TWO_THOUSAND", 4: "FIVE_THOUSAND"}
    return switch[value_number]
