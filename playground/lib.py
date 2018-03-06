def get_lines (line_count = 2):

    txt = ''

    for n in range(1, line_count + 1):

        txt += 'Line ' + str(n) + '\n'

    return txt



def get_lines_2 ( args = {} ):

    #get vars from args
    if 'count' in args:
        count = args['count']
    else:
        count = 5

    if 'pre' in args:
        pre = args['pre']
    else:
        pre = 'TEST'

    #rationalize args
    if count < 1:
        count = 1

    #create output
    txt = ''

    for n in range(1, count + 1):

        txt += pre + ' ' + str(n) + '\n'

    return txt