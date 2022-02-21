from .config import NFT_NAME, DESCRIPTION, BASE_URI, EXTERNAL_URL, FILE_TYPE, ADD_RARITY

def get_keys_and_values(nft):
    attributes = []
    for key,value in nft.items():
        if value == None:
            continue
        if key != 'rarity' and value != None:
            traits = {
                "trait_type" : key, 
                "value" : value
                }
        else:
            if ADD_RARITY:
                traits = {
                    "display_type": "number",
                    "trait_type" : key, 
                    "value" : value
                }
        attributes.append(traits)
    return attributes

def complex_nft_dict(nft):
    nft = {
                "name" : f"{NFT_NAME}#{nft['edition']}",
                "image" : f"{BASE_URI}/{nft['edition']}{FILE_TYPE}",
                "description" : DESCRIPTION,
                "external_url" : EXTERNAL_URL,
                "edition": nft['edition'],
                "attributes": get_keys_and_values(nft)
            }
    return nft