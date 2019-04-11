
import os, sys
from shutil import copyfile
import tkinter as tk
from tkinter import filedialog as fd
root = tk.Tk()
root.withdraw()

#path = "C:\\jon\\_temp\\mcrm"
path = "L:\\cbt_published\\MCRM_Maritime"
cssFile = "C:\\jon\\python\\mcrm\\customStyle.css"

folders = []
#folders.append("02 Human Performance and Limitations")
folders.append("03 Attitudes")
#folders.append("04 Situational Awareness")
#folders.append("05 Cultural Awareness")
#folders.append("06 Communications and Briefings")
#folders.append("07 Authority and Assertiveness")
#folders.append("08 Challenge and Response")
#folders.append("09 Short Term Strategy")
#folders.append("10 Workload")
#folders.append("11 Humans and Automation")
#folders.append("12 Team")
#folders.append("13 Error Management")
#folders.append("14 Leadership Styles")
#folders.append("15 Decision Making")
#folders.append("16 Crisis Management")
#folders.append("17 Crowd Management")
#folders.append("18 Critical Incident Debriefing")


searchString = '<html lang="en">\n<head>'
replaceString = '<html lang="en">\n<head>\n<link href="customStyle.css" type="text/css" rel="stylesheet">'

# get published dir
options = {}
options['initialdir'] = path
options['title'] = 'MCRM published directory:'
t = fd.askdirectory(**options)

if t:
    path = t
else:
    sys.exit("Operation Cancelled")


# update files
updateCount = 0

for folder in folders:
    indexFile = path + "\\" + folder + "\\index.html"

    # check file exists
    if not os.path.isfile(indexFile):
        print(indexFile + " does not exist; SKIPPING!!!!")
        continue

    # copy css file
    print("Copying CSS file....", end="")
    destFile = path + "\\" + folder + "\\customStyle.css"
    copyfile(cssFile, destFile)
    if os.path.isfile(destFile):
        print("OK")
    else:
        print("ERROR!!!! CSS file NOT copied!")


    # open index.html
    print("modifying " + indexFile + "....", end="")
    htmlFile = open(indexFile, "r")
    html = htmlFile.read()
    htmlFile.close()

    # check file contains searchString
    found = html.find(replaceString)
    if found != -1:
        print("SKIPPING: HTML already modified!!!!")
        continue

    # replace in file
    html = html.replace(searchString, replaceString)

    # write to file
    htmlFile = open(indexFile, "w")
    result = htmlFile.write(html)
    htmlFile.close()

    if result:
        updateCount += 1
        print("OK")
    else:
        print("ERROR!!!!!!")


print("Finished! " + str(updateCount) + " files updated.")
