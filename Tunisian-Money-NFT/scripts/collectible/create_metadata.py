from brownie import MoneyCollectible, network
from scripts.helpful_scripts import get_value
from metadata import sample_metadata
from pathlib import Path
import os
import requests
import json
def main():
    print("Working on " + network.show_active())
    money_collectible = MoneyCollectible[len(MoneyCollectible) - 1]
    number_of_money_collectibles = money_collectible.tokenCounter()
    print("The number of tokens you've deployed is: "+ str(number_of_money_collectibles))
    write_metadata(number_of_money_collectibles, money_collectible)
    
def write_metadata(number_of_money_collectibles, nft_contract):
    for token_id in range(number_of_money_collectibles):
        collectible_metadata = sample_metadata.metadata_template
        value = get_value(nft_contract.tokenIdToValue(token_id))
        metadata_file_name = (
            "./metadata/{}/".format(network.show_active())
            + str(token_id)
            + "-"
            + value
            + ".json"
        )
        if Path(metadata_file_name).exists():
            print("{} Already Found !".format(metadata_file_name))
        else:
            print("Creating Metadata File {}".format(metadata_file_name))
            collectible_metadata["name"] = get_value(
                nft_contract.tokenIdToValue(token_id))
            collectible_metadata["description"] = "This is worth {} millimes".format(collectible_metadata["name"])
            #print(collectible_metadata)
            image_to_upload = None
            if os.getenv("UPLOAD_IPFS") == "True":
                image_path = "./img/{}.jpg".format(
                    value.lower().replace("_","-"))
                image_to_upload = upload_to_ipfs(image_path)
            collectible_metadata["image"] = image_to_upload
            with open(metadata_file_name, 'w') as file:
                json.dump(collectible_metadata,file)
            if os.getenv("UPLOAD_IPFS") =="True":
                upload_to_ipfs(metadata_file_name)


def upload_to_ipfs(filepath):
    with Path(filepath).open("rb") as fp:
        image_binary = fp.read()
        ipfs_url = "http://localhost:5001"
        response = requests.post(
            ipfs_url + "/api/v0/add", files={"file": image_binary})
        ipfs_hash = response.json()["Hash"]
        print("first file name is : {}".format(filepath))
        filename = filepath.split("/")[-1:][0]
        print(filename)
        uri = "https://ipfs.io/ipfs/{}?filename={}".format(
            ipfs_hash,filename)
        print(uri)
        return uri
    return None
        
                
                

