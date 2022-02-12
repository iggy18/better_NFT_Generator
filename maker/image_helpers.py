from PIL import Image

def cleaned(attribute_file):
    pic = Image.open(attribute_file)
    if pic.mode != "RGBA":
        pic = pic.convert("RGBA")
    return pic

def stack_images(bottom, top):
    return Image.alpha_composite(bottom, top)