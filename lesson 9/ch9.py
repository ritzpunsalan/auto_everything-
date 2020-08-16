""" 
chapter 9
    Lists
pg 197 - 214
"""
# 198
# cmd python
# ctrl + z to exit
"""

# The shutil Module

# Copying Files and Folders

import shutil
import os

os.chdir('C:\\')
shutil.copy('C:\\spam.txt', 'C:\\delicious')

shutil.copy('eggs.txt', 'C:\\delicious\\eggs2.txt')

does not work!! 

"""
# 199
# cmd python
# ctrl + z to exit
"""

import shutil
import os
os.chdir('C:\\')
shutil.copytree('C:\\bacon', 'C:\\bacon_backup')

# Moving and Renaming Files and Folders

import shutil
shutil.move('C:\\bacon.txt', 'C:\\eggs')


shutil.move('C:\\bacon.txt', 'C:\\eggs\\new_bacon.txt')


shutil.move('C:\\bacon.txt', 'C:\\eggs')

does not work!!

"""
# 200
# cmd python
# ctrl + z to exit
"""

shutil.move('spam.txt', 'c:\\does_not_exist\\eggs\\ham')

# Permanently Deleting Files and Folders

works sort of !!

"""
# 201
# cmd python
# ctrl + z to exit
"""

# Safe Deletes with the send2trash Module

import send2trash
baconFile = open('bacon.txt', 'a')  # creates the file
baconFile.write('Bacon is not a vegetable.')

baconFile.close()
send2trash.send2trash('bacon.txt')

does not work!!

"""
# 204
# cmd python
# ctrl + z to exit
"""

# Reading ZIP Files

import zipfile
import os
os.chdir('C:\\')  # move to the folder with example.zip
exampleZip = zipfile.ZipFile('example.zip')
exampleZip.namelist()

spamInfo = exampleZip.getinfo('spam.txt')
spamInfo.file_size

spamInfo.compress_size

'Compressed file is %sx smaller!' % (round(spamInfo.file_size / spamInfo.compress_size, 2))

exampleZip.close()

does not work!!

"""
# 205
# cmd python
# ctrl + z to exit
"""

# Extracting from ZIP Files

os.chdir('C:\\')  # move to the folder with example.zip
exampleZip = zipfile.ZipFile('example.zip')
exampleZip.extractall()
exampleZip.close()

exampleZip.extract('spam.txt')

exampleZip.extract('spam.txt', 'C:\\some\\new\\folders')

exampleZip.close()

# Creating and Adding to ZIP Files

newZip = zipfile.ZipFile('new.zip', 'w')
newZip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)
newZip.close()

does not work!!

"""