import cfg
cfg.init()
import lib
import glob
import os
import sys
import shutil


# runtime flags
includeRTimages = False





# set directories
dirsOK = lib.setDirectories()

if not dirsOK:
    sys.exit('build cancelled')






# set searchString, i.e. what folders to include in build

userInput = input('What lessons shall we build? Current searchString is (' + cfg.searchString + ') ')

if userInput:
    cfg.searchString = userInput











# empty output folder?

if os.listdir(cfg.outputDir) != []:

    userInput = input('outputDir (' + cfg.outputDir + ') is not empty, empty it? (yes/no) ')

    if userInput == 'y' or userInput == 'yes':
        print('emptying folder ' + cfg.outputDir + '....', end='')
        result = lib.emptyFolder(cfg.outputDir)
        if result:
            print('OK')
        else:
            sys.exit('ERROR: Folder not emptied. Stopping build.')
    else:
        print('Will NOT empty ' + cfg.outputDir)








# get lesson folders
os.chdir(cfg.contentDir)
lessonFolders = []
for file in glob.glob(cfg.searchString + '*'):
    lessonFolders.append(file)









# create lesson folders in cfg.outputDir
for folder in lessonFolders:

    myDir = cfg.outputDir + '/' + folder
    print('making folder ' + myDir + '....', end='')
    result = lib.createDir(myDir)

    if result:
        print('OK')
    else:
        sys.exit('ERROR!!!!')





# create content folders (1 in each lesson folder)
for folder in lessonFolders:

    myDir = cfg.outputDir + '/' + folder + '/content'
    print('making folder ' + myDir + '....', end='')
    result = lib.createDir(myDir)

    if result:
        print('OK')
    else:
        sys.exit('ERROR!!!!')






# copy library files
print('Copying system / lib files (this could take a few minutes)....')
item = 1

for folder in lessonFolders:

    for libFolder in cfg.libFolders:

        sourceDir = cfg.libDir + '/' + libFolder
        destDir = cfg.outputDir + '/' + folder + '/' + libFolder
        print('copying from ' + sourceDir + ' to ' + destDir + '....', end='')
        shutil.copytree(sourceDir, destDir)

        if os.path.isdir(destDir):
            print('OK (' + str(item) + '/' + str(len(lessonFolders)) + ')')
        else:
            sys.exit('ERROR: ' + destDir + ' not copied!!')

    item = item + 1




# copy RT Images?
if includeRTimages:

    for folder in lessonFolders:

        print('Copying RT images....', end='')
        sourceDir = cfg.libDir + '/RT'
        destDir = cfg.outputDir + '/' + folder + '/images/rt'
        shutil.copytree(sourceDir, destDir)

        if os.path.isdir(destDir):
            print('OK')
        else:
            sys.exit('ERROR: ' + destDir + ' not copied!!')








# copy lesson files
print('Copying lesson files (this could take a few minutes)....')
item = 1
for folder in lessonFolders:

    sourceDir = cfg.contentDir + '/' + folder
    destDir = cfg.outputDir + '/' + folder + '/content/' + folder
    print('copying from ' + sourceDir + ' to ' + destDir + '....', end='')
    shutil.copytree(sourceDir, destDir)

    if os.path.isdir(destDir):
        print('OK (' + str(item) + '/' + str(len(lessonFolders)) + ')')
    else:
        sys.exit('ERROR: ' + destDir + ' not copied!!')

    item = item + 1




# finished
print('FINISHED')