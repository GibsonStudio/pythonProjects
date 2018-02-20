__author__ = 'jwilliams'

import glob
import os


def check_product(code):

    error_list = []

    path = 'L:\\cbt_video_published\\content\\'
    #os.chdir(dir)

    dirs = os.listdir(path)

    for dir in dirs:

        if dir[:len(code)] == code:

            output = 'checking lesson ' + dir + '....'
            lesson_dir = path + "\\" + dir + "\\"
            os.chdir(lesson_dir)
            result = check_lesson(False)

            if len(result) > 0:

                error_list.append("\n>>>>>>>> " + dir + ' >>>>>>>>')
                error_list.extend(result)
                output += 'SOME NOT USED!!!'

            else:

                output += 'OK'

            print(output)

    return error_list







def check_lesson(show_output = True):

    error_list = []

    for file in glob.glob('*.*'):

        output = 'checking that ' + file + ' is used....'

        if file_used(file):

           output += 'OK'

        else:

           output += 'NOT USED!!!!'
           error_list.append(file)

        if show_output:

            print(output)

    return error_list













def get_file_extension(filename):

    return filename[filename.rfind('.') + 1:]





def remove_file_extension(filename):

    return filename[:filename.rfind('.')]








def file_used(file_to_check):

    #ignore ini_lesson.js - this is required!!
    if file_to_check == 'ini_lesson.js':

        return True

    #if .mp4, check used using add_video('');
    if get_file_extension(file_to_check) == 'mp4':

        for file in glob.glob('*.html'):

            if "add_video('" + remove_file_extension(file_to_check) + "')" in open(file).read():

                return True


    #if mp3, check used by RT call javascript
    if get_file_extension(file_to_check) == 'mp3':

        for file in glob.glob('*.html'):

            if "rt.id = '" + remove_file_extension(file_to_check) + "';" in open(file).read():

                return True



    #check used in js
    for file in glob.glob('*.js'):

        if file_to_check in open(file).read():

            return True


    #check used in css
    for file in glob.glob('*.css'):

        if file_to_check in open(file).read():

            return True


    #check used in html
    for file in glob.glob('*.html'):

        if file_to_check in open(file).read():

            return True


    return False





