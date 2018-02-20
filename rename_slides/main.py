
# rename slides

import glob
import os
import sys

source_dir = 'L:\\small random projects\\quality and compliance\\slides\\'
output_folder = 'output\\'

os.chdir(source_dir)

for img in glob.glob('*.JPG'):

    source_file = source_dir + img

    new_name = img.replace('Slide', 'slide_')
    new_name = new_name.replace('JPG', 'jpg')

    # get number and add leading zero if required
    underscore_pos = new_name.index('_')
    dot_pos = new_name.index('.')
    slide_num = new_name[underscore_pos + 1:dot_pos]

    if int(slide_num) < 10:
        slide_num = '0' + str(slide_num)
    else:
        slide_num = str(slide_num)

    new_name = new_name[:underscore_pos + 1] + slide_num + new_name[dot_pos:]

    result = 'Renaming ' + img + ' to ' + new_name + '....'

    os.rename(source_dir + img, source_dir + output_folder + new_name)

    if os.path.isfile(source_dir + output_folder + new_name):
        result += 'OK'
    else:
        result += 'FAIL!!!'

    print(result)


