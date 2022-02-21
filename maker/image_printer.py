import os
from collections import OrderedDict

from tqdm import tqdm
from .image_helpers import cleaned, stack_images
from .generate import lottery
from .config import FILE_TYPE, LAYER_ORDER
from .strings import RERUN

PROJECT = project = os.listdir('input')

def compose(images):
    base = None
    for img in images:
        if base is None:
            base = cleaned(img)
        else:
            base = stack_images(base, cleaned(img))
    return base

def in_path(attribute, value):
    return f'input/{attribute}/{value}{FILE_TYPE}'

def out_path(edition):
    return f'results/images/{edition}{FILE_TYPE}'

def ordered(nft):
    od = OrderedDict()
    for item in LAYER_ORDER:
        if item in nft:
            od[item] = nft[item]
    return od

def make_image(nft):
    edition = nft['edition']
    path_list = []
    organized = ordered(nft)
    for attribute, value in organized.items():
        if attribute in PROJECT and value != None:
            path_list.append(in_path(attribute, value))
    completed_image = compose(path_list)
    completed_image.save(out_path(edition))


def build_paths():
    try:
        to_print = lottery()
        for nft in tqdm(to_print):
            pass
            make_image(nft)
    except:
        print(RERUN)