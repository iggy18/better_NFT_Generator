import random

from .checks import ensure_output_folders_exist
from .config import WEIGHTS, NUMBER_OF_DESIRED_IMAGES, ADD_RARITY, OPTIONAL_LAYERS, NUMBER_OF_DESIRED_IMAGES, LUCKY_NUMBERS, CONFLICTING_TRAITS, LAYER_ORDER
from .inputs import get_files, missing_input_folders
from .strings import NFTS_ASSEMBLED, REVIEW_MESSAGE, RARE
from .writers import rarity_json, init_CSV, write_to_CSV, individual_json, json_metadata
from .nft_json_template import complex_nft_dict

TRAITS_AND_VALUES = get_files()

def tally_values(nft_list):
    res = {key:dict() for key in LAYER_ORDER}
    for outer_dict in nft_list:
        for key, value in outer_dict.items():
            if key != 'edition':
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
        #to_csv.append(nft['edition'])
        # go through main dict here
        for layer in LAYER_ORDER:
            if layer in nft:
                to_csv.append(nft[layer])
            else:
                nft[layer] = None
                to_csv.append(nft[layer])
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
    edition = 0
    for nft in nft_list:
        nft['edition'] = edition
        edition += 1

def add_rarity_score_to_nft(rarity_tally, nft_list):
    for nft in nft_list:
        score = 0
        count = 0
        for trait, value in nft.items():
            if trait != 'edition':
                count += 1
                score += rarity_tally[trait][value]
        nft['rarity'] = score

def winner():
    number = random.randint(1, NUMBER_OF_DESIRED_IMAGES)
    if number in LUCKY_NUMBERS:
        print(RARE)
        return True
    
def roll_for_optional_layers(nft):
    for layer in OPTIONAL_LAYERS:
                    if winner():
                        nft[layer] = None
                        nft[layer] = random.choices(TRAITS_AND_VALUES[layer], weights=WEIGHTS[layer], k=1)[0]

def remove_conflicting_traits(nft):
    for key, value in nft.items():
        if key in CONFLICTING_TRAITS:
            if key in nft:
                print(nft[key])
                for item in CONFLICTING_TRAITS[key]:
                    nft[item] = None

                ################################ THIS is the problem area is it key or value???

def acceptable():
    keep = input(REVIEW_MESSAGE)
    if keep == 'yes':
        return True
    else:
        return False

def lottery():
    
    ensure_output_folders_exist()
    
    if missing_input_folders():
        return
    
    unique_nfts = []
    
    def generate_unique_nft():
        nft = {}
        nft['edition'] = None
        for key, value in TRAITS_AND_VALUES.items():
            if key != 'edition' and key not in OPTIONAL_LAYERS:
                nft[key] = random.choices(value, weights=WEIGHTS[key], k=1)[0]
        
        if OPTIONAL_LAYERS:
            roll_for_optional_layers(nft)
        
        if CONFLICTING_TRAITS:
            remove_conflicting_traits(nft)
                        
        if nft in unique_nfts:
            return generate_unique_nft()
        
        return nft

    for i in range(0, NUMBER_OF_DESIRED_IMAGES):
        unique_nfts.append(generate_unique_nft())
    
    rarity_dict = tally_values(unique_nfts)
    
    if ADD_RARITY:
        add_rarity_score_to_nft(rarity_dict, unique_nfts)
    
    rarity_json(rarity_dict)
    
    if not acceptable():
        return
    
    add_edition_to(unique_nfts)
    
    init_CSV()
    
    make_csv(unique_nfts)
    
    create_json_files(unique_nfts)
    
    print(NFTS_ASSEMBLED)
    
    return unique_nfts