import cfg
import os
import shutil
import tkinter as tk
from tkinter import filedialog as fd
root = tk.Tk()
root.withdraw()



def setDirectories():

    # get outputDir
    # get lib dir
    options = {}
    options['initialdir'] = cfg.outputDir
    options['title'] = 'output directory:'
    t = fd.askdirectory(**options)

    if t:
        cfg.outputDir = t
    else:
        return False

    return True








def createDir(newDir):

    if os.path.isdir(newDir):
        return True

    os.makedirs(newDir)

    if os.path.isdir(newDir):
        return True

    return False




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