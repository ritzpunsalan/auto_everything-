""" 
chapter 5
    Lists
pg 105 - 122
"""
# 105
# The Dictionary Data Type
"""

myCat = {'size': 'fat', 'color': 'grey', 'disposition': 'loud'}
print(myCat)

works!!

"""
# 106
"""

myCat = {'size': 'fat', 'color': 'grey', 'disposition': 'loud'}
print(myCat['size'])
print('My cat has ' + myCat['color'] + ' fur.')

works!!

"""
"""

spam = {12345: 'Luggage Combination', 42: 'The Answer'}
print(spam)

works!! sort of

"""
# Dictionaries vs Lists
"""
spam = ['cats', 'dogs', 'moose']
bacon = ['dogs', 'moose', 'cats']
print(spam == bacon)

eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'}
print(eggs == ham)

works!!

"""

"""

spam = {'name': 'Zophie', 'age': 7}
spam['color']

does not work!!

"""