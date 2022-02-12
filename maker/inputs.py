import os

from .strings import EMPTY_INPUT, NO_INPUT

def input_folder_does_not_exist():
    if not os.path.exists('input'):
        os.mkdir('input')
        print(NO_INPUT)
        return True

def input_folder_is_empty():
    if not os.listdir('input'):
        print(EMPTY_INPUT)
        return True
    
def remove_ext(filenames):
    clean_file_names = []
    for file in filenames:
        clean_file_names.append(file.split('.')[0])
    return clean_file_names
    
def missing_input_folders():
    if input_folder_does_not_exist() or input_folder_is_empty():
        return True


def get_files():

    dir_path_dict = {}
    #this makes the most sense as placement for this check
    if missing_input_folders():
        return 

    for (dirpath, dirnames, filenames) in os.walk('input'):
        feature = dirpath.split('/')[-1]
        
        #maybe add no files feedback
        if filenames:
            clean_text_list = remove_ext(filenames)
            dir_path_dict[feature] = clean_text_list
    return dir_path_dict