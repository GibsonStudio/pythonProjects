__author__ = 'jwilliams'

import os
import lib

#user defined vars
path    = 'L:\\cbt_video_published\\content\\';
lesson  = 'EL-2-Current'
code    = 'FM' #setting code will check an entire product, set to 'HU-', 'IFR-', 'EG-' ect..


dir = path + lesson + "\\"
os.chdir(dir)




if code:

    result = lib.check_product(code)

else:

    print('checking the lesson ' + dir + '....')
    result = lib.check_lesson()


print("\nNOT USED:")

for file in result:

    print(file)


