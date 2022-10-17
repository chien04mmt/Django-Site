#Import Image class from PIL module
from PIL import Image

def RESIZE_IMAGE(path_image):
    
    image = Image.open(path_image)
    width, height = image.size
    w=400
    h=height/(width/w)
    new_image = image.resize(( int(w) , int(h) ))
    new_image.save(path_image)

    # print(image.size) # Output: (1920, 1280)
    # print(new_image.size) # Output: (400, 400)
