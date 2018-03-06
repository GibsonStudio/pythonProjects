__author__ = 'jwilliams'

import glob
import os
import re

#note 1: the r prefix denotes a raw string ad is required if you are capturing groups
#note 2: groups are returned with \1, \2 etc...
#note 3: if index is set to any integer > 0, it will be incremented and added to each replace string <index>

folder = 'C:\\jon\\temp\\rename\\'
rule = r'ASE'
replace = r'ase'
index = 0
leading_zero = True


os.chdir(folder)

for file in glob.glob('*'):

    filename = file

    if index > 0:

        this_index = str(index)

        if index <= 9 and leading_zero:
            this_index = '' + this_index
            this_replace = replace.replace('<index>', '0' + str(index))

        else:
            this_replace = replace.replace('<index>', str(index))


        index += 1

    else:
        this_replace = replace

    new_filename = re.sub(rule, this_replace, filename)
    result = 'Renaming ' + filename + ' to ' + new_filename + '....'

    os.rename(folder + filename, folder + new_filename)

    if os.path.isfile(folder + new_filename):
        result += 'OK'
    else:
        result += 'FAIL!!!'

    print(result)


