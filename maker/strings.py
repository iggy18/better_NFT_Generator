from colorama import init, Fore
init(autoreset=True)

EMPTY_INPUT = Fore.RED + 'The input folder does not contain any folders or files. please place attribute folders into input folder'

INPUT_FOUND = Fore.GREEN + 'Input attributes sucessfully gathered'

NO_INPUT = Fore.YELLOW + 'There was no input folder\nA new input folder has been created,\nbut you will need to add the attribute folders and files before restarting the program'

FINISHED = Fore.GREEN + 'nft metadata has been assembled. review rarity.json file'

NFTS_ASSEMBLED = Fore.GREEN + 'NFT ingredients succesfully collected and mixed. baking images now...'