import os

def ensure_output_folders_exist():
    required_dirs = ['results', 'results/json', 'results/images', 'results/csv']
    for folder in required_dirs:
        if not os.path.exists(folder):
            os.mkdir(folder)