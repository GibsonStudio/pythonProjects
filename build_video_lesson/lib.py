
def create_file (filepath, content):

    my_file = open(filepath, 'w')
    my_file.write(content)
    my_file.close()

    if my_file:
        return 'OK'
    else:
        return 'ERROR'




def create_html_file(filepath, video_file):

    my_file = open(filepath, 'w')

    html = '<!DOCTYPE HTML>\n\n'
    html += '<html>\n\n'
    html += '<head>\n'
    html += '\t<script type="text/javascript" src="../../javascript/lib.js"></script>\n'
    html += '\t<script>write_head();</script>\n'
    html += '</head>\n\n'
    html += '<body onLoad="scene_loaded()" class="noselect">\n\n'
    html += '\t<script>write_header();write_nav();</script>\n'
    html += '\t<script>add_video(\'' + video_file + '\');</script>\n\n'
    html += '</body>\n\n'
    html += '</html>'

    my_file.write(html)
    my_file.close()

    if my_file:
        return 'OK'
    else:
        return 'ERROR'



def clean_string (s):

    import re

    #convert ampersand
    s = re.sub('\&', 'and', s)

    #escape quote
    s = re.sub('\'', '\\\'', s)

    return s

