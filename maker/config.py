# the name of your collection.
NFT_NAME = 'Doodle Doods'

# the description of your collection
DESCRIPTION = "the result of a python code tutorial"

# enter number of desired images here
NUMBER_OF_DESIRED_IMAGES = 20

# enter the type of image file you are using including the '.'
FILE_TYPE = '.png'

#base uri/CID you get from IPFS
BASE_URI = 'ipfs://{REPLACE_WITH_CID}'

# any website you want to link to
EXTERNAL_URL = 'https://www.{REPLACE_WITH_WEBSITE}.com'

# True if you want rarity score on csv False if you don't
ADD_RARITY= True

#the order of the layers in the image from left to right (top to bottom)
LAYER_ORDER = ["background", "head", "hair", "nose", "mouth", "eyes", "body", "arms", "logo", "ears", "hat"]

# "folder name: [10, 40, 60, 30, 1]"
WEIGHTS = {
    "background" : [10, 40, 60, 3, 20, 30, 20],
    "head" : [10, 15, 20, 5, 20, 30],
    "hair" : [5, 10, 30, 40],
    "nose" : [30, 40, 8, 30, 25],
    "mouth" : [4, 12, 25, 30, 15],
    "eyes" : [11, 9, 15, 12, 11, 10, 10, 12, 17, 6, .5],
    "body" : [10, 30, 30, 2, 22, 32, 20, 12],
    "arms" : [50, 50, 10],
    "logo" : [60, 40],
    "ears" : [10, 40, 60, 30, 25],
    "hat" : [100]
}

#(((((((((((((((((((((((((((((((ADVANCED OPTIONS)))))))))))))))))))))))))))))))

# layers that are optional. not every image will contain them
# leave empty if you don't have optional layers
OPTIONAL_LAYERS = ["logo", "hat"]

# for use with optional layers
# if you have a trait that can not exist with other traits, add it here 
# ex: 
# "sunglasses" : ["eyes"],
# "motorcycleHelmet" : ["eyes", "ears", "hat", "nose", "mouth"]
# if a motorcycle helmet is picked, 
# the eyes, ears, hat, nose, and mouth will be removed from the image
# this is done to keep the meta data clean 
# so attributes that aren't in the image are not included in the meta data
CONFLICTING_TRAITS = {
    "hat" : ["ears", "mouth", "hair"]
}

# for optional layers. must be between 1 and desired number of images. 
# the more numbers you have the more likely it is for the image to have that layer 
LUCKY_NUMBERS = [2, 5]
