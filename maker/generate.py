import random

from .checks import ensure_output_folders_exist
from .config import WEIGHTS, NUMBER_OF_DESIRED_IMAGES, ADD_RARITY
from .inputs import get_files, missing_input_folders
from .strings import NFTS_ASSEMBLED
from .writers import rarity_json, init_CSV, write_to_CSV, individual_json, json_metadata
from .nft_json_template import complex_nft_dict

TRAITS_AND_VALUES = get_files()

def tally_values(nft_list):
    res = {key:dict() for (key, value) in nft_list[0].items()}
    for outer_dict in nft_list:
        for key, value in outer_dict.items():
            if value in res[key]:
                res[key][value] += 1
            else:
                res[key][value] = 0
    #get rarity score here
    for attr, dic in res.items():
        if key != 'edition':
            for key, value in dic.items():
                res[attr][key] = value / NUMBER_OF_DESIRED_IMAGES
    return res

def make_csv(nft_list):
    to_csv = []
    for nft in nft_list:
        for key, value in nft.items():
            to_csv.append(value)
        write_to_CSV(to_csv)
        to_csv = []

def create_json_files(nft_list):
    meta = []
    for nft in nft_list:
        res = complex_nft_dict(nft)
        meta.append(res)
    for nft in meta:
        individual_json(nft)
    json_metadata(meta)
    
def add_edition_to(nft_list):
    edition = 1
    for nft in nft_list:
        nft['edition'] = edition
        edition += 1

def add_rarity_score_to_nft(rarity_tally, nft_list):
    for nft in nft_list:
        score = 0
        count = 0
        for trait, value in nft.items():
            count += 1
            score += rarity_tally[trait][value]
        nft['rarity'] = score
    

def lottery():
    
    ensure_output_folders_exist()
    
    if missing_input_folders():
        return
    
    init_CSV()
    
    unique_nfts = []
    
    def generate_unique_nft():
        nft = {}
        nft['edition'] = None
        for key, value in TRAITS_AND_VALUES.items():
            if key != 'edition':
                nft[key] = random.choices(value, weights=WEIGHTS[key], k=1)[0]
        if nft in unique_nfts:
            return generate_unique_nft()
        return nft

    for i in range(0, NUMBER_OF_DESIRED_IMAGES):
        unique_nfts.append(generate_unique_nft())
    
    rarity_dict = tally_values(unique_nfts)
    
    if ADD_RARITY:
        add_rarity_score_to_nft(rarity_dict, unique_nfts)
    
    rarity_json(rarity_dict)
    
    add_edition_to(unique_nfts)
    
    make_csv(unique_nfts)
    
    create_json_files(unique_nfts)
    
    print(NFTS_ASSEMBLED)
    
    return unique_nfts