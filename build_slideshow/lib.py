
# build slideshow lib

import os
import glob


def get_files (dir, ext):

    os.chdir(dir)
    files = []

    for file in glob.glob('*.jpg'):
        files.append(file)

    return files




def create_file (filepath, content):

    my_file = open(filepath, 'w')
    my_file.write(content)
    my_file.close()

    if my_file:
        return 'OK'
    else:
        return 'ERROR'





def get_html_file_contents (img):

    html = '<!DOCTYPE HTML>\n\n'
    html += '<html>\n\n'
    html += '<head>\n'
    html += '\t<script type="text/javascript" src="../../javascript/lib.js"></script>\n'
    html += '\t<script>write_head();</script>\n'
    html += '</head>\n\n'
    html += '<body onLoad="scene_loaded();radio_ini();" class="noselect">\n\n'
    html += '\t<script>write_header();write_nav();</script>\n'
    html += '\t<div id="content" class="content_center" style="padding:0px;">\n'
    html += '\t\t<img style="width: 100%; max-width: 1024px;" src="' + img + '" />\n'
    html += '\t</div>\n\n'
    html += '</body>\n\n'
    html += '</html>'

    return html




def get_ini_lesson_contents (files):

    ini_contents = 'var lesson_title = "LESSON_TITLE";\n\n'
    ini_contents += 'var my_scenes = [];\n\n'
    ini_contents += 'my_scenes = [];\n'

    for i in range(0, len(files)):

        if i == 0:
            filename = 'index'
        else:
            filename = remove_file_extension(files[i])

        ini_contents += 'my_scenes.push(["' + filename + '.html", "' + remove_file_extension(files[i]) + '"]);\n'

    return ini_contents







def remove_file_extension (filename):

    dot = len(filename) - filename.rfind('.')
    return filename[:-dot]