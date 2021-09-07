from brownie import MoneyCollectible, network, accounts, config
from scripts.helpful_scripts import get_value

money_metadata_disc = {
    "FIVE_THOUSAND": "https://ipfs.io/ipfs/QmUDpYzfKwUDvSzQZAqEhkd7RuRUaC5wnN6ZZHWDbZ28E6?filename=0-FIVE_THOUSAND.json",
    "ONE_HUNDRED": "https://ipfs.io/ipfs/QmNaqqTAAuEkXkues7jqExZtfK9SKEYNQyR3zApr1uRuXW?filename=one-hundred.json",
    "TWO_THOUSAND": "https://ipfs.io/ipfs/QmcdeTXnP7zW9fSdkW19NqSbmanhoFKHgAg1xKRrcJ6CzM?filename=0-TWO_THOUSAND.json",
    "ONE_THOUSAND": "https://ipfs.io/ipfs/QmSkQTkpjgmK11sLA4fcd3p3aydbQasjsUEY49YK5tv1ZN?filename=0-ONE_THOUSAND.json"
}
OPENSEA_FORMAT = "https://testnets.opensea.io/assets/{}/{}"

def main():
    print("Working on " + network.show_active())
    money_collectible = MoneyCollectible[len(MoneyCollectible) - 1]
    number_of_money_collectibles = money_collectible.tokenCounter()
    print(
        "The number of tokens you've deployed is: "
        + str(number_of_money_collectibles)
    )
    for token_id in range(number_of_money_collectibles):
        value = get_value(money_collectible.tokenIdToValue(token_id))
        if not money_collectible.tokenURI(token_id).startswith("https://"):
            print("Setting tokenURI of {}".format(token_id))
            set_tokenURI(token_id,money_collectible,money_metadata_disc[value])
        else:
            print("skip {}, we've already set that tokenURI:".format(token_id))
def set_tokenURI(token_id, nft_contract, tokenURI):
    dev = accounts.add(config["wallets"]["from_key"])
    nft_contract.setTokenURI(token_id,tokenURI,{"from":dev})
    print("awesome you can now view your NFT at {}".format(
        OPENSEA_FORMAT.format(nft_contract.address,token_id)
    ))
    print("Please give up to 20 min and hit the 'refresh metadata' button")
