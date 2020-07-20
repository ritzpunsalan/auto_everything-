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
# birthdays.py
# 107
"""

birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated.')

works!!

"""

# 108
# The Dictionary Data Type
"""

spam = {'color': 'red', 'age': 42}
for v in spam.values():
    print(v)

for k in spam.keys():
    print(k)

for i in spam.items():
    print(i)

spam = {'color': 'red', 'age': 42}
print(spam.keys())

print(list(spam.keys()))

spam = {'color': 'red', 'age': 42}
for k, v in spam.items():
    print('key: ' + k + ' Value: ' + str(v))

works!!

"""

# 109
# Checking Whether a Key or Value Exists in a Dictionary
"""

spam = {'name': 'Zophie', 'age': 7}
print('name' in spam.key())

print('Zophie' in spam.values())

print('color' in spam.keys())

print('color' not in spam.keys())

print('color' in spam)

# The get() Method

picnicItems = {'apples': 5, 'cups': 2}
print('I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.')

print('I am bringing ' + str(picnicItems.get('cups', 0)) + ' eggs.')

# picnicItems = {'apples': 5, 'cups': 2}
# print('I am bringing ' + str(picnicItems.['eggs']) + ' cups.')

does not work properly!!

"""
# 110
# The setdefault() Method
"""

# spam = {'name:' 'Pooka', 'age': 5}
# if 'color' not in spam:
#     spam['color'] = 'black'

# spam = {'name:' 'Pooka', 'age': 5}
# print(spam.setdefault('color', 'black'))

# # spam
# print(spam)
# # spam.setdefault('color', 'white')
# print(spam.setdefault('color', 'white'))

# # spam
# print(spam)

# characterCount.py

message = 'It was a bright cold day in april, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print(count)


sort of works!!

"""
# 111
# Pretty Printing

# PrettyCharacterCount.py
"""

import pprint
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)

works!!

"""
#115
# ticTacToe.py
"""

TheBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
printBoard(TheBoard)

TheBoard = {'top-L': 'O', 'top-M': 'O', 'top-R': 'O',
            'mid-L': 'X', 'mid-M': 'X', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': 'X'}
def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
printBoard(TheBoard)

works!!

"""
# 116
# ticTacToe.py
"""

TheBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}


def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])


turn = 'X'
for i in range(9):
    printBoard(TheBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    TheBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
printBoard(TheBoard)

works ! !

"""
# 118
"""

allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1}}


def totalBrought(guest, item):
    numBrought = 0
    for k, v in guest.items():
        numBrought = numBrought + v.get(item, 0)
    return numBrought


print('Number of things being brought:')
print(' - Apples         ' + str(totalBrought(allGuests, 'apples')))
print(' - Cups           ' + str(totalBrought(allGuests, 'cups')))
print(' - Cakes          ' + str(totalBrought(allGuests, 'cakes')))
print(' - Ham Sandwiches ' + str(totalBrought(allGuests, 'ham sandwiches')))
print(' - Apple Pies     ' + str(totalBrought(allGuests, 'apple pies')))

works!!

"""