

import glob
import os, sys
from PIL import Image

source_folder = 'L:\\small random projects\\quality and compliance\\slides\\'
output_folder = 'output2\\'
image_size = 768, 576

os.chdir(source_folder)

for img in glob.glob('*.jpg'):

    source_file = source_folder + img
    #img = img.replace('Slide', 'slide_')
    #img = img.replace('JPG', 'jpg')
    output_file = source_folder + output_folder + img

    message = 'resizing ' + img + '....'

    try:
        im = Image.open(source_file)
        im.thumbnail(image_size, Image.ANTIALIAS)
        im.save(output_file, "JPEG")
        message += 'OK'
    except IOError:
        message += 'ERROR'

    print(message)


print('finished.')


