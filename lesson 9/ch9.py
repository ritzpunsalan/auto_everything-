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