
import os
import glob

upload_dir = 'C:\\wamp\\www\\caeoaaappforms\\uploads\\user\\'
user_count = 468

for i in range(5, user_count + 1):

    user_dir = upload_dir + str(i) + '\\'

    if os.path.isdir(user_dir):

        print('Updating user ' + user_dir + '....')
        os.chdir(user_dir)

        #.jpgs
        for file in glob.glob('*.jpg.jpg'):

            current_name = user_dir + file
            new_name = user_dir + file[:-4]
            print('renaming ' + current_name + ' to ' + new_name)
            os.rename(current_name, new_name)
            print('renamed OK....')

        #.pngs
        for file in glob.glob('*.png.png'):

            current_name = user_dir + file
            new_name = user_dir + file[:-4]
            print('renaming ' + current_name + ' to ' + new_name)
            os.rename(current_name, new_name)
            print('renamed OK....')