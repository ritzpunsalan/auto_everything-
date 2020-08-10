""" 
chapter 8
    Lists
pg 173 - 196
"""
# 174
# cmd python
# ctrl + z to exit
"""
# Backslash on Windows and Forward Slash on OS X and Linux

import os
os.path.join('usr', 'bin', 'spam')


myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in myFiles:

works sort of!! 

"""
# 175
# cmd python
# ctrl + z to exit
"""

# The Current Working Directory

os.getcwd()

os.chdir('C:\\Windows\\System32')
os.getcwd()


os.chdir('C:\\ThisFolderDoesNotExist')

# Absolute vs. Relative Paths

works!!

"""
# 176
# cmd python
# ctrl + z to exit
"""

# Creating New Folders with os.makedirs()

import os
os.makedirs('C:\\delicious\\walnut\\waffles')

# os.makedirs('E: \Desktop\neccessy books for coding\python books\automate python\\pilot\\directories')

works sort of !!

"""
# 177
# cmd python
# ctrl + z to exit
"""

# The os.path Module

# Handling Absolute and Relative Paths

os.path.abspath('.')

os.path.abspath('.\\Scripts')

os.path.isabs('.')

os.path.isabs(os.path.abspath('.'))

# important note
# very dangerous to mess with if not knowing properly.
# ^^^^ ^^^^^^^^^

works sort of!!

"""
# 178
# cmd python
# ctrl + z to exit
"""

os.path.relpath('C:\\Windows', 'C:\\')

os.path.relpath('C:\\Windows', 'C:\\spam\\eggs')

os.getcwd()


path = 'C:\\Windows\\System32\\calc.exe'
os.path.basename(path)

os.path.dirname(path)

calcFilePath = 'C:\\Windows\\System32\\calc.exe'
os.path.split(calcFilePath)

(os.path.dirname(calcFilePath), os.path.basename(calcFilePath))

# important note
# very dangerous to mess with if not knowing properly.
# ^^^^ ^^^^^^^^^

works sort of !!

"""
# 179
# cmd python
# ctrl + z to exit
"""

calcFilePath.split(os.path.sep)

'/usr/bin'.split(os.path.sep)

# Finding File Sizes and Folder Contents

os.path.getsize('C:\\Windows\\System32\\calc.exe')

os.listdir('C:\\Windows\\System32')


totalSize = 0
for filename in os.listdir('C:\\Windows\\System32'):
totalSize = totalSize + \
    os.path.getsize(os.path.join('C:\\Windows\\System32', filename))

print(totalSize)

# important note
# very dangerous to mess with if not knowing properly.
# ^^^^ ^^^^^^^^^

does not work properly!!

"""
# 180
# cmd python
# ctrl + z to exit

# Checking Path Validity
"""

os.path.exists('C:\\Windows')

os.path.exists('C:\\some_made_up_folder')

os.path.isdir('C:\\Windows\\System32')

os.path.isfile('C:\\Windows\\System32')

os.path.isdir('C:\\Windows\\System32\\calc.exe')

os.path.isfile('C:\\Windows\\System32\\calc.exe')


os.path.exists('D:\\')

# The File Reading/Writing Process

# important note
# very dangerous to mess with if not knowing properly.
# ^^^^ ^^^^^^^^^

does not work!!

"""
# 181
# cmd python
# ctrl + z to exit
"""

# Opening Files with the open() Function

helloFile = open('C:\\Users\\your_home_folder\\hello.txt')

helloFile = open('/Users/your_home_folder/hello.txt')

# important note
# very dangerous to mess with if not knowing properly.
# ^^^^ ^^^^^^^^^

does not work!!

"""
# 182
# cmd python
# ctrl + z to exit
"""

# Reading the Contents of Files

helloContent = helloFile.read()
helloContent

sonnetFile = open('sonnet29.txt')
sonnetFile.readlines()

# important note
# very dangerous to mess with if not knowing properly.
# ^^^^ ^^^^^^^^^

does not work!!

"""
# 183
# cmd python
# ctrl + z to exit
"""

# Writing to Files

baconFile = open('bacon.txt', 'w')
baconFile.write('Hello world!\n')

baconFile.close()
baconFile = open('bacon.txt', 'a')
baconFile.write('Bacon is not a vegetable.')

baconFile.close()
baconFile = open('bacon.txt')
content = baconFile.read()
baconFile.close()
print(content)

# important note
# very dangerous to mess with if not knowing properly.
# ^^^^ ^^^^^^^^^

works!!

"""
# 184
# cmd python
# ctrl + z to exit
"""

# Saving Variables with the shelve Module

import shelve
shelfFile = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
shelfFile.close()


shelfFile = shelve.open('mydata')
type(shelfFile)

shelfFile['cats']

shelfFile.close()

# important note
# very dangerous to mess with if not knowing properly.
# ^^^^ ^^^^^^^^^

works sort of!!

"""