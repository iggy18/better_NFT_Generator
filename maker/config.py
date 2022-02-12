# the name of your collection.
NFT_NAME = 'Skullmon'

# the description of your collection
DESCRIPTION = "the result of a python code tutorial"

# enter number of desired images here
NUMBER_OF_DESIRED_IMAGES = 100

# enter the type of image file you are using including the '.'
FILE_TYPE = '.png'

# True if you want rarity score on csv False if you don't
ADD_RARITY= True

#the order of the layers in the image from left to right
LAYER_ORDER = ["background", "head", "mouth", "eyes"]

# "folder name: [10, 40, 60, 30, 1]"
WEIGHTS = {
    "eyes" : [10, 3, 60, 30, 15, 20],
    "head" : [10, 40, 60, 30, 6],
    "mouth" : [10, 40, 60, 30, 1],
    "background" : [10, 40, 60, 30, 1],
}

#base uri/CID you get from IPFS
BASE_URI = 'ipfs://{REPLACE_ME}'

EXTERNAL_URL = 'https://www.seth.mcfeeters.com'