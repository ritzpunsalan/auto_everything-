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