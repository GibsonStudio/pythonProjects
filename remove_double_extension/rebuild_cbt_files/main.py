__author__ = 'jwilliams'

import glob
import os

import lib


#fixed vars
lessonFile = 'L:\\software\\tools\\lesson maker\\finished\\system files\\lesson.swf'

#config vars
sourceDir = 'L:\\cbt_published\\atpl_aircraft performance\\content\\'
destDir = 'C:\\jon\\temp\\ap\\'

os.chdir(sourceDir)

for file in glob.glob('*.xml'):

    filename = file[:-4]

    #make dir
    result = ''
    tDir = destDir + filename + '\\'
    result += 'Creating dir ' + tDir + '....'
    if not os.path.exists(tDir):
        os.mkdir(tDir)
    result += str(os.path.exists(tDir))
    print(result)

    #make xx-xxx-xxx.swf
    result = ''
    my_file = filename + '.swf'
    dest = tDir + my_file
    result += 'Creating file ' + dest + '....'
    result += lib.create_file(dest,lessonFile)
    print(result)

    #make xx-xxx-xxx.html
    result = ''
    my_file = filename + '.html'
    dest = tDir + my_file
    result += 'Creating file ' + dest + '....'
    result += lib.create_html_file(dest, filename)
    print(result)


