
# build slideshow
# build 1

import lib


dir = 'L:\\small random projects\\quality and compliance\\slides\\output\\'
lesson_title = 'My Lesson'


# get file list as array
files = lib.get_files(dir, '.jpg')

# write ini_lesson.js
print('creating ini_lesson.js....')
ini_file = dir + 'ini_lesson.js'
ini_contents = lib.get_ini_lesson_contents(files)
result = lib.create_file(ini_file, ini_contents)
print(result)


# write html files
print('building html files....')

for i in range(0, len(files)):

    if i == 0:
        html_file = 'index.html'
    else:
        html_file = lib.remove_file_extension(files[i]) + '.html'

    html = lib.get_html_file_contents(files[i])

    print('creating ' + html_file + '...')

    result = lib.create_file(dir + html_file, html)
    print(result)



print('finished.')





