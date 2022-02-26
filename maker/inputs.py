import glob, os

from .strings import EMPTY_INPUT, NO_INPUT
from .config import FILE_TYPE


def make_value_dictionary():
    files = glob.glob(f'input/*/*{FILE_TYPE}')
    
    value_dict = dict()

    for file in files:
        items = file.split('/')
        trait = items[-2]
        value = items[-1].split('.')[0]
        value_dict[trait] = value_dict.get(trait, []) + [value]
        
    return value_dict

def input_folder_does_not_exist():
    if not os.path.exists('input'):
        os.mkdir('input')
        print(NO_INPUT)
        return True

def input_folder_is_empty():
    if not os.listdir('input'):
        print(EMPTY_INPUT)
        return True
    
def missing_input_folders():
    if input_folder_does_not_exist() or input_folder_is_empty():
        return True


def get_files():

    if missing_input_folders():
        return 

    return make_value_dictionary()