# input
- place individual folders in the input folder
- each folder should contain all layers for one type of nft attribute
- the name of each folder will be the name of your trait types
- the name of each file will be the name of your values 
- ** WARNING: there can be no repeated names for folders or files. All folders and files must have unique names **
- ** WARNING: folders and files can not contain numbers, spaces or special characters. **

# results
- the results folder is created when the program is run
- after the program is done you will find your images and metadata in the results folder
- if you drag and drop the results folder somewhere else, or delete the results folder entirely, the program will automatically create a new results folder for you when run again

# Config
- inside the lib folder is a file called config. you will need to add your values there.
- under the advanced options you will find config for optional layers

# Instructions
- fill out the config file (in the "maker" folder) with your values
- run the program by typing `pythhon __main__.py` in the terminal
- you will be prompted to review the rarity.json file
- if everything looks good, type "yes" to continue
- the program will then create a new folder called "results"
- inside the results folder you will find your images and metadata
- if you do not like the results, you can delete the entire results folder and run the program again
- once you are happy with the results you can upload your entire images folder to IPFS
- after the upload is complete you want to copy the CID for the folder and come back to your IDE
- hopefully your IDE will have a universal "find all and replace" feature
- find all instances of `{REPLACE_WITH_CID}` and replace them with the CID
- this should change the link to the image for all JSON files in your results folder so they now point to the IPFS folder containing your images
- then you can upload the JSON files to IPFS


- use a test net first and make sure everything works before you move to the main net
- so far this metadata has only been tested on opensea