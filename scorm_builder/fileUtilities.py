import cfg
import os
import shutil

import tkinter as tk
from tkinter import filedialog as fd
root = tk.Tk()
root.withdraw()

def getDirectories ():

    # get lib dir
    options = {}
    options['initialdir'] = cfg.libDir
    options['title'] = 'lib directory:'
    t = fd.askdirectory(**options)

    if t:
        cfg.libDir = t
    else:
        return False



    # get content dir
    options = {}
    options['initialdir'] = cfg.contentDir
    options['title'] = 'content directory:'
    t = fd.askdirectory(**options)

    if t:
        cfg.contentDir = t
    else:
        return False



    # get output dir
    options = {}
    options['initialdir'] = cfg.outputDir
    options['title'] = 'output ditrctory:'
    t = fd.askdirectory(**options)

    if t:
        cfg.outputbDir = t
    else:
        return False

    return True




def emptyFolder (path):

    for fileobj in os.listdir(path):

        objPath = os.path.join(path, fileobj)
        if os.path.isfile(objPath):
            os.unlink(objPath)
        elif os.path.isdir(objPath):
            shutil.rmtree(objPath)

    # check dir is empty and return boolean
    if len(os.listdir(path)) == 0:
        return True

    return False




def copyFolder (sourceDir, destDir):
    # copy sourceDir folders to destDir
    for path, subdirs, files in os.walk(sourceDir):
        if len(subdirs) > 0:
            for sd in subdirs:
                newPath = os.path.join(path, sd).replace(sourceDir, destDir)
                os.makedirs(newPath)

    # copy sourceDir files to destDir
    for path, subdirs, files in os.walk(sourceDir):
        for name in files:
            sourceFile = os.path.join(path, name)
            destFile = os.path.join(path.replace(sourceDir, destDir), name)
            shutil.copy(sourceFile, destFile)

    return True



def createDir (newDir):
    os.makedirs(newDir)
    if os.path.isdir(newDir):
        return True

    return False