__author__ = 'jwilliams'

def create_file(file, lessonFile):

    import shutil
    res = shutil.copyfile(lessonFile, file)

    if res:
        return 'OK'
    else:
        return 'ERROR'






def create_html_file(file, filename):

    my_file = open(file, 'w')

    html = '<HTML>\n\n'
    html += '<HEAD>\n'
    html += '\t<TITLE>' + filename + '</TITLE>\n'
    html += '</HEAD>\n\n'
    html += '<BODY style="background: #4863a0; margin: 0px;">\n\n'
    html += '\t<OBJECT><EMBED src="' + filename + '.swf" width="100%" height="100%" quality="high"/></OBJECT>\n\n'
    html += '</BODY>\n\n'
    html += '</HTML>'

    my_file.write(html)
    my_file.close()

    if my_file:
        return 'OK'
    else:
        return 'ERROR'


