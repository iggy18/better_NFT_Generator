import os

head = ['blue', 'red', 'orange', 'green', 'black']
eyes = ['big', 'small', 'cross', 'wide', 'narrow', 'one', 'three', 'brown', 'wink', 'unimpressed', 'doubtful']
mouth = ['frown', 'smile', 'smirk', 'open', 'flat']
nose = ['roman', 'crooked', 'thin', 'flared', 'giant']
hair =['long', 'short', 'bald', 'afro', 'bowl', 'shaggy', 'halfshaved', 'undercut', 'mohawk', 'flattop']

arrarr = {'head':head, 'eyes':eyes, 'mouth': mouth, 'nose':nose, 'hair': hair}

def ensure_output_folders_exist():
    required_dirs = ['results', 'results/json', 'results/images', 'results/csv']
    for folder in required_dirs:
        if not os.path.exists(folder):
            os.mkdir(folder)

def setup_input_folders():
    required_dirs = ['input', 'input/head', 'input/eyes', 'input/nose', 'input/mouth', 'input/hair']
    for item in required_dirs:
        if not os.path.exists(item):
            os.mkdir(item)


def setup_files(attributes):
    for folder, files in attributes.items():
        for file in files:
            if not os.path.exists(f'input/{folder}/{file}.txt'):
                os.mknod(f'input/{folder}/{file}.txt')

def start():
    ensure_output_folders_exist()
    setup_input_folders()
    setup_files(arrarr)