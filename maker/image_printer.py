import os
from collections import OrderedDict

from tqdm import tqdm
from .image_helpers import cleaned, stack_images
from .generate import lottery
from .config import FILE_TYPE, NFT_NAME, LAYER_ORDER

PROJECT = project = os.listdir('input')

def compose(imges):
    base = None
    for img in imges:
        if base is None:
            base = cleaned(img)
        else:
            base = stack_images(base, cleaned(img))
    return base

def in_path(attribute, value):
    return f'input/{attribute}/{value}{FILE_TYPE}'

def out_path(edition):
    return f'results/images/{NFT_NAME}#{edition}{FILE_TYPE}'

def ordered(nft):
    od = OrderedDict()
    for item in LAYER_ORDER:
        od[item] = nft[item]
    return od

def make_image(nft):
    edition = nft['edition']
    path_list = []
    organized = ordered(nft)
    for attribute, value in organized.items():
        if attribute in PROJECT:
            path_list.append(in_path(attribute, value))
    completed_image = compose(path_list)
    completed_image.save(out_path(edition))


def build_paths():
    to_print = lottery()
    for nft in tqdm(to_print):
        make_image(nft)