""" 
chapter 4
    Lists
pg 79 - 104
"""
# 80

# The list data type
"""

print([1, 2, 3])
print(['cat', 'bat', 'rat', 'elephant'])
print(['hello', 3.1415, True, None, 42])
spam = ['cat', 'bat', 'rat', 'elephant']
print(spam)

works!!

"""

# Getting Individual Values in a List with Indexes
"""

spam = ['cat', 'bat', 'rat', 'elephant']
print(spam[0])
print(spam[1])
print(spam[2])
print(spam[3])
print(['cat', 'bat', 'rat', 'elephant'][3])
print('Hello ' + spam[0])
print('The ' + spam[1] + ' ate the ' + spam[0] + '.')

works!! 

"""
# 81

"""

spam = ['cat', 'bat', 'rat', 'elephant']
print(spam[10000])

error works!!

"""

"""

spam = ['cat', 'bat', 'rat', 'elephant']
print(spam[1])
print(spam[1.0])

error works!!

"""

"""

spam = [['cat', 'bat'], [10, 20, 30, 40, 50]]
print(spam[0])
print(spam[0][1])
print(spam[1][4])

works!!

"""
# 82
# Negative Indexes
"""

spam = ['cat', 'bat', 'rat', 'elephant']
print(spam[-1])
print(spam[-3])
print('The ' + spam[1] + ' is afraid of the ' + spam[3] + '.')

works!!

"""
# Getting Sublists with Slices
"""

spam = ['cat', 'bat', 'rat', 'elephant']
print(spam[0:4])
print(spam[1:3])
print(spam[0:-1])

works!!

"""

"""

spam = ['cat', 'bat', 'rat', 'elephant']
print(spam[:2])
print(spam[1:])

works!!

"""
# 83
# Getting a  List's length with len()
"""

spam = ['cat', 'dog', 'moose']
print(len(spam))

works!!

"""
# Changing Values in a List with Indexes
"""

spam = ['cat', 'bat', 'rat', 'elephant']
spam[1] = 'aardvark'
print(spam)
spam[2] = spam[1]
print(spam)
spam[-1] = 12345
print(spam)

works!!

"""
# List Concatenation and List Replication
"""
print([1, 2, 3] + ['A', 'B', 'c'])
print(['X', 'Y', 'Z'] * 3)
spam = [1, 2, 3]
spam = spam + ['A', 'B', 'C']
print(spam)

works!!

"""
# 84
# Removing Values from Lists with del Statements
"""

spam = ['cat', 'bat', 'rat', 'elephant']
del spam[2]
print(spam)
del spam[2]
print(spam)

works!!

"""
# allMyCats1.py
# Working with Lists
"""

print('Enter the name of cat 1:')
catName1 = input()
print('Enter the name of cat 2:')
catName2 = input()
print('Enter the name of cat 3:')
catName3 = input()
print('Enter the name of cat 4:')
catName4 = input()
print('Enter the name of cat 5:')
catName5 = input()
print('Enter the name of cat 6:')
catName6 = input()
print('The cat names are:')
print('catName1 + ' ' + catName2 +' ' + catName3 +' ' + catName4 + ' ' + catName5 + ' ' + catName6')

works but an error in the end!!

"""
# allMyCats2.py
# 85
# Working with Lists
"""

catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) +
          ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name]  # last concatenation
print('The cat names are:')
for name in catNames:
    print('  ' + name)

works!!

"""
# 86
# Using for Loops with Lists
"""

for i in range(4):
    print(i)

works!!

"""

"""

for i in [0, 1, 2, 3]:
    print(i)

work!!

"""
"""

supplies = ['pens', 'staples', 'flames-throwers', 'binders']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

works!! 

"""
# 87
# The in and not in Operators
"""

print('howdy' in ['hello', 'hi', 'howdy', 'heyas'])
spam = ['hello', 'hi', 'howdy', 'heyas']
print('cat' in spam)

print('howdy' not in spam)

print('cat' not in spam)

works!!

"""
# myPets.py
"""

myPets = ['Zophie', 'Pooka', 'Fat-tail']
print('Enter a pet name:')
name = input()
if name not in myPets:
    print('I do not have a pet named ' + name)
else:
    print(name + ' is my pet.')

works!! 

"""
# The Multiple Assignment Trick
"""

cat = ['fat', 'black', 'loud']
size = cat[0]
color = cat[1]
disposition = cat[2]

cat = ['fat', 'black', 'loud']
size, color, disposition = cat

does not work!!

"""
# 88
# Augmented Assignment Operators
"""

spam = 42
spam = spam + 1
print(spam)

spam = 42
spam += 1
print(spam)

spam = 'Hello'
spam += ' world!'
print(spam)

bacon = ['Zophie']
bacon *= 3
print(bacon)

works!!

"""
# 89
# Methods
# Finding a Value in a List with the index() Method
"""

spam = ['hello', 'hi', 'howdy', 'heyas']
print(spam.index('hello'))

print(spam.index('heyas'))

print(spam.index('howdy howdy howdy'))

spam = ['Zophie', 'Pooka', 'Fat-tail', 'Pooka']
print(spam.index('Pooka'))

# AddingValuestoLists with theappend() and insert()Methods

spam = ['cat', 'dog', 'bat']
spam.append('moose')
print(spam)

works!!

"""
# 90
"""

spam = ['cat', 'dog', 'bat']
spam.insert(1, 'chicken')
print(spam)

works!!

"""
"""

eggs = 'hello'
eggs.append('world')
print(eggs)

bacon = 42
bacon.insert(1, 'world')
print(bacon)

does not work properly!!

"""
# Removing Values from Lists with remove()
"""

spam = ['cat', 'bat', 'rat', 'elephant']
spam.remove('bat')
print(spam)

works!!

"""
# 91
"""

spam = ['cat', 'bat', 'rat', 'elephant']
spam.remove('chicken')
print(spam)

does not work properly!!

"""
"""

spam = ['cat', 'bat', 'rat', 'cat', 'hat', 'cat']
spam.remove('cat')
print(spam)

works!!

"""
# Sorting the Values in a List with the sort() Method
"""

spam = [2, 5, 3.14, 1, -7]
spam.sort()
print(spam)
spam = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
spam.sort()
print(spam)

spam.sort(reverse=True)
print(spam)

works!!

"""

# 92
"""

 spam = [1, 3, 2, 4, 'Alice', 'Bob']
 spam.sort()

works improperly!!

import random
spam = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']
spam.sort()
print(spam)

spam = ['a', 'z', 'A', 'Z']
spam.sort(key=str.lower)
print(spam)

# Example Program: Magic 8 Ball with aList
# magic8ball2.py

messages = ['It is certain',
            'It is decidedly so',
            'Yes definitely',
            'Reply hazy try again',
            'Ask again later',
            'Concentrate and ask again',
            'My reply is no',
            'Outlook not so good',
            'Very doubtful']

print(messages[random.randint(0, len(messages) - 1)])

all works!!

"""

# 93
"""

spam = ['apples',
        'oranges',
        'bananas',
        'cats']
print(spam)

print('four score and seven ' +
      'years ago...')

works!!

"""
# 94
"""

name = 'Zophie'
# name[0]
# name[-2]
# name[0:4]
# print(name)
print('Zo' in name)
print('z' in name)
print('p' not in name)
'Zo' in name
'z' in name
'p' not in name
for i in name:
    print('*** ' + i + ' ***')

works sort of!!

# Mutable and ImmutableDataTypes

# name = 'Zophie a cat'
# name[7] = 'the'

works improperly!!

name = 'Zophie a cat'
newName = name[0:7] + 'the' + name[8:12]
print(name)
print(newName)

works!!

"""
# 95
"""

eggs = [1, 2, 3]
eggs = [4, 5, 6]
print(eggs)

eggs = [1, 2, 3]
del eggs[2]
del eggs[1]
del eggs[0]
eggs.append(4)
eggs.append(5)
eggs.append(6)
print(eggs)

works!!

"""
# 96
"""

# The Tuple Data type

eggs = ('hello', 42, 0.5)
print(eggs[0])
print(eggs[1:3])
print(len(eggs))

works!!

eggs = ('hello', 42, 0.5)
# print(eggs[1] = 99)

works!! error

"""

# 97
"""

print(type(('hello',)))
print(type(('hello')))

# Converting Types with the list() and tuple() function

print(tuple(['cat', 'dog', 5]))
print(list(('cat', 'dog', 5)))
print(list('hello'))

# references

spam = 42
cheese = spam
spam = 100
print(spam)
print(cheese)

works!!

"""
# 98
"""

spam = [0, 1, 2, 3, 4, 5]
cheese = spam
cheese[1] = 'Hello!'
print(spam)
print(cheese)

works!!

"""