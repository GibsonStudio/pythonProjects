# imports
import cfg
cfg.init()
import fileUtilities as fu
import sys
import os
import zipfile
#import shutil
#import glob



# start main

#dirsOK = fu.getDirectories()

#if not dirsOK:
#    sys.exit('SCORM cancelled')


# change to contentDir and get files

#os.chdir(cfg.libDir)

#for file in glob.glob('*.*'):
#    print(file)


# empty output dir?
#TODO remove temp confirm override
"""
if len(os.listdir(cfg.outputDir)) > 0:
    userInput = 'yes' #input('outputDir (' + cfg.outputDir + ') is not empty, empty it? (yes/no) ')
    if userInput == 'yes':
        print('emptying output folder....', end='')
        result = fu.emptyFolder(cfg.outputDir)
        if result:
            print('OK')
        else:
            sys.exit('ERROR: outputDir is not empty, build aborted.')
    else:
        sys.exit('cannot proceed as outputDir is not empty')



# copy lib files to outputFolder
print('copying lib files....', end='')
result = fu.copyFolder(cfg.libDir, cfg.outputDir)
if result:
    print('OK')
else:
    sys.exit('ERROR: lib files not copied.')


# create content dir
print('creating content dir....', end='')
contentDir = os.path.join(cfg.outputDir, 'content')
if fu.createDir(contentDir):
    print('OK')
else:
    sys.exit('content dir not created.')



# copy content files
print('copying content files....', end='')
if fu.copyFolder(cfg.contentDir, contentDir):
    print('OK')
else:
    sys.exit('content files not copied.')
"""

#TODO create imsmanifest.xml

iniFile = os.path.join(cfg.contentDir, 'ini_lesson.js')
iniData = []
f = open(iniFile, 'r')
for line in f:
    iniData.append(line)
f.close()

lessonTitle = ''
scenes = []
for line in iniData:
    if line.startswith('var lesson_title'):
        startChar = int(line.find('\'')) + 1
        endChar = int(line.rfind('\''))
        lessonTitle = line[startChar:endChar]
    elif line.startswith('my_scenes.push'):
        line = line.replace('\', \'', '\',\'')
        startChar = int(line.find('([')) + 3
        endChar = int(line.rfind('\',\''))
        fileName = line[startChar:endChar]
        startChar = int(line.find('\',\'')) + 3
        endChar = int(line.rfind('])')) - 1
        sceneName = line[startChar:endChar]
        scenes.append([fileName, sceneName])

print(scenes)

sys.exit('STOP')


#build scorm.zip archive
archiveName = 'scorm_01.zip'
print('building zip archive....', end='')
archiveFiles = []
for path, subdirs, files in os.walk(cfg.outputDir):
    for name in files:
        myFile = os.path.join(path.replace(cfg.outputDir, ''), name)
        if myFile.startswith('\\'):
            myFile = myFile[1:]
        archiveFiles.append(myFile)

os.chdir(cfg.outputDir)
zip = zipfile.ZipFile(archiveName, 'a')
for file in archiveFiles:
    zip.write(file)
zip.close()

if os.path.isfile(os.path.join(cfg.outputDir, archiveName)):
    print('OK')
    print('Finished!')
else:
    sys.exit('zip archive not created')



