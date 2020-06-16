"""
    source link:
E:\Desktop\neccessy books for coding\python books\automate python
E:\Desktop\neccessy books for coding\python books
E:\Desktop\neccessy books for coding\python books\automate python\testrun

"""
# chapter: 5
# This program says hello and asks for my name.

# allMyCats1.py
# 106
# The Dictionary Data Type

# myCat = {'size': 'fat', 'color': 'grey', 'disposition': 'loud'}
# print(myCat['size'])
# print('My cat has ' + myCat['color'] + ' fur.')

spam = {12345: 'Luggage Combination', 42: 'The Answer'}
print(spam)

# Dictionaries vs Lists

spam = ['cats', 'dogs', 'moose']
bacon = ['dogs', 'moose', 'cats']
spam == bacon

eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'}
eggs = ham

spam = {'name': 'Zophie', 'age': 7}
spam['color']