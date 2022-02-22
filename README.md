# Python NFT Art Generator
<img src="https://github.com/iggy18/better_NFT_Generator/blob/main/examples/13.png" alt="drawing" width="200"/> <img src="https://github.com/iggy18/better_NFT_Generator/blob/main/examples/14.png alt="drawing" width="200"/>


<img src="https://github.com/iggy18/better_NFT_Generator/blob/main/examples/21.png" alt="drawing" width="200"/> <img src="https://github.com/iggy18/better_NFT_Generator/blob/main/examples/32.png" alt="drawing" width="200"/>



# input


- place individual folders in the input folder


- each folder should contain all layers for one type of nft attribute


- the name of each folder will be the name of your trait types


- the name of each file will be the name of your values 


**WARNING: there can be no repeated names for folders or files. All folders and files must have unique names**


**WARNING: folders and files can not contain numbers, spaces or special characters.**



# results


- the results folder is created when the program is run. if you do not see this folder it means that the has not been run yet. 


- after the program is done you will find your images and metadata in the results folder


- if you drag and drop the results folder somewhere else, or delete the results folder entirely, the program will automatically create a new results folder for you when run again



# Config


- inside the lib folder is a file called config. you will need to add your values there.


- under the advanced options you will find config for optional layers


- if you have optional layers you will need lucky numbers. you may need to adjust the amount of lucky numbers you have so optional layers are chosen more or less frequently


- lucky numbers only work if they are between 1 and the number of desired images. so if you ask for 20 images and the lucky number is 21, the optional layer will never be chosen.


- if you have a layer that contains images which cover other layers, you want to add that layer to the CONFLICTING_LAYERS list in the config file.


- CONFLICTING_LAYERS is a dictionary. the key is the name of the layer that is conflicting. the value is a list of layers that will be removed if that layer is selected.


- layers are removed to keep the metadata file, and CSV file, clean. this way you won't have attributes showing up on opensea that aren't in th image. 


# Instructions


- fill out the config file (in the "maker" folder) with your values


- run the program by typing `python make_art.py` in the terminal


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

# Notes

- use a test net first and make sure everything works before you move to the main net


- so far the metadata has only been tested on opensea

- at the moment this program only generates the art and metadata. 


- you'll need to add the metadata to IPFS yourself, deploy the contract, and mint the NFTs.


- I will continue to work on this program to make it as much of a one stop shop as I can.

- the next step for this project will be to add the ability to upload images and metadata to IPFS automatically...