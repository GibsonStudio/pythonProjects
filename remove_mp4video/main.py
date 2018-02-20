__author__ = 'jwilliams'

import glob
import os

folder = 'E:\\raw_video\\atpl_pe\\PE-pro-pr5\\'
remove = '.mp4video'

os.chdir(folder)

for file in glob.glob('*.mp4'):

    filename = file

    c = filename.count(remove)

    if c > 0:

        new_filename = filename.replace('.mp4video', '')
        result = 'Renaming ' + filename + ' to ' + new_filename + '....'

        os.rename(folder + filename, folder + new_filename)

        if os.path.isfile(folder + new_filename):
            result += 'OK'
        else:
            result += 'FAIL!!!'

        print(result)


