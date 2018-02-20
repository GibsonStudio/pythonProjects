
#build 1
#08/10/2015

import vars
import lib
import glob
import os
import re
import sys

nav = vars.get_nav()
read_nav = True
scene_num = 1
dir = 'L:\\cbt_video_published\\content\\PPL05-air-air\\'
os.chdir(dir)
lesson_name = nav.get('lesson_name', 'Lesson')

#remove full stop from end of lesson_name
lesson_name = re.sub(r'\.$', '', lesson_name)
lesson_name = lib.clean_string(lesson_name)

#start to build ini_lesson.js
last_scene = ''
ini = 'var lesson_title = \'' + lesson_name + '\';\n'
ini += 'var my_scenes;\n'
ini += 'my_scenes = [];\n'


print('BUILDING HTML FILES FROM GLOB LIST:')

#build files from glob

for file in glob.glob('*.mp4'):

    video_file = file[:-4]
    scene_number = re.sub(r'.*-s', '', video_file)

    if scene_number == '01':
        filename = 'index.html'
    else:
        filename = video_file + '.html'

    filepath = dir + filename
    output = 'Creating file ' + filename + '....'
    output += lib.create_html_file(filepath, video_file)

    print(output)

    #add to ini_lesson.js

    if read_nav:

        last_scene = nav.get('Scene ' + scene_number, last_scene)

        if scene_number == '01':
            ini += 'my_scenes.push([\'index.html\', \'' + lib.clean_string(last_scene) + '\']);\n'
        else:
            ini += 'my_scenes.push([\'' + video_file + '.html\', \'' + lib.clean_string(last_scene) + '\']);\n'

    else:

        if scene_number == '01':
            ini += 'my_scenes.push([\'index.html\', \'Scene\']);\n'
        else:
            ini += 'my_scenes.push([\'' + video_file + '.html\', \'Scene\']);\n'



ini_file = dir + 'ini_lesson.js'
output = 'Creating ' + ini_file + '....'
output += lib.create_file(ini_file, ini)

print(output)




