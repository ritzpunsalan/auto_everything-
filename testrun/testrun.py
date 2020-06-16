"""
    source link:
E:\Desktop\neccessy books for coding\python books\automate python
E:\Desktop\neccessy books for coding\python books
E:\Desktop\neccessy books for coding\python books\automate python\testrun

"""
# chapter: 4
# This program says hello and asks for my name.

# allMyCats1.py
# 87
# The in and not in Operators

# print('howdy' in ['hello', 'hi', 'howdy', 'heyas'])
# spam = ['hello', 'hi', 'howdy', 'heyas']
# print('cat' in spam)

# print('howdy' not in spam)

# print('cat' not in spam)

# myPets.py

myPets = ['Zophie', 'Pooka', 'Fat-tail']
print('Enter a pet name:')
name = input()
if name not in myPets:
    print('I do not have a pet named ' + name)
else:
    print(name + ' is my pet.')

# # The Multiple Assignment Trick

# cat = ['fat', 'black', 'loud']
# size = cat[0]
# color = cat[1]
# disposition = cat[2]

# cat = ['fat', 'black', 'loud']
# size, color, disposition = cat
