""" 
chapter 6
    Lists
pg 123 - 146
"""
# 124
# cmd python
# ctrl + z to exit
"""

# Strings Literals

# Double Quotes

spam = "that is Alice's cat."

# Escape Characters

spam = 'Say hi to Bob\'s  mother.'

works!!

"""

# 125
# cmd python
# ctrl + z to exit
"""

print("Hello there!\nHow are you?\nI\'m doing fine. ")

# Raw Strings

print(r'That is Carol\'s cat.')

# Multiline Strings with Triple Quotes
# catnapping.py

print('''Dear alice, 

Eve's cat has been arrested for catnapping, cat burglary, and extortion.

Sincerely,
Bob''')

works!!

"""
# 126
"""

print('Dear alice,\n\nEve\'s cat has been arrested for catnapping, cat burglary, and extortion.\n\nSincerely,\nBob')

# Multiline Comments

# ### this is a test Python program.
# written by Al Sweigart al@inventwithpython.com

# this program was designed for Python 3, not Python 2.
# ###


# def spam():
#     ### this is a multiline comment to help
#     explain what the spam() function does.###
#     print('Hello!')

# Indexing and Slicing Strings
# cmd python
# ctrl + z to exit


spam = 'Hello world!'
spam[0]

spam[4]

spam[-1]

spam[0:5]

spam[:5]

spam[6:]

works!! sort of. had to replace the triple " to ###

"""
# 127
# cmd python
# ctrl + z to exit
"""

spam = 'Hello world!'
fizz = spam[0:5]
fizz

# The in and out in Operators with Strings

'Hello' in 'Hello World'

'Hello' in 'Hello'

'HellO' in 'Hello World'

'' in 'spam'

'cats' not in 'cats and dogs'

works!!

"""
# 128
# cmd python
# ctrl + z to exit
"""

# The upper(), lower(), isupper(), and islower() String Methods

spam = 'Hello world!'
spam = spam.upper()
spam

spam = spam.lower()
spam

print('How are you?')
feeling = input()
if feeling.lower() == 'great':
    print('I feel great too.')
else:
    print('I hope the rest of your day is good.')

works!!

"""
# 129
# cmd python
# ctrl + z to exit
"""

spam = 'Hello world!'
spam.islower()

spam.isupper()

'HELLO'.isupper()

'abc12345'.islower()

'12345'.islower()

'12345'.isupper()


'Hello'.upper()

'Hello'.upper().lower()

'Hello'.upper().lower().upper()

'HELLO'.lower()

'HELLO'.lower().islower()

# The isX String Methods

works!!

"""

# 130
# cmd python
# ctrl + z to exit
"""

'hello'.isalpha()

'hello123'.isalpha()

'hello123'.isalnum()

'hello'.isalnum()

'123'.isdecimal()

' '.isspace()

'This Is Title Case'.istitle()

'This Is Title Case 123'.istitle()

'This Is not Title Case'.istitle()

'This Is NOT Title Case Either'.istitle()

# validateInput.py

while True:
    print('Enter your age:')
    age = input()
    if age.isdecimal():
        break
    print('Please enter a number for your age.')

while True:
    print('Select a new password (letters and numbers only):')
    password = input()
    if password.isalnum():
        break
    print('Passwords can only have letters and numbers.')

works!!

"""
# 131
# cmd python
# ctrl + z to exit
"""

# The startswith() and endswith() String Methods

'Hello world!'.startswith('Hello')

'Hello world!'.endswith('world!')

'abc123'.startswith('abcdef')

'abc123'.endswith('12')

'Hello world!'.startswith('Hello world!')

'Hello world!'.endswith('Hello world!')

# The join() and split() String Methods

works!!

"""
# 132
# cmd python
# ctrl + z to exit
"""

', '.join(['cats', 'rats', 'bats'])

' '.join(['My', 'name', 'is', 'Simon'])

'ABC'.join(['My', 'name', 'is', 'Simon'])


'My name is Simon'.split()


'MyABCnameABCisABCSimon'.split('ABC')

'My name is Simon'.split('m')


spam = '''Dear Alice,
How have you been? I am fine.
There is a container in the fridge
that is labeled "Milk Experiment".
Please do not drink it.
Sincerely,
Bob'''

spam.split('\n')

works!!

"""
# 133
# cmd python
# ctrl + z to exit

# Justifying Text with rjust(), ljust(), and center()
"""

'Hello'.rjust(10)

'Hello'.rjust(20)

'Hello World'.rjust(20)

'Hello'.ljust(10)


'Hello'.rjust(20, '*')

'Hello'.ljust(20, '-')


'Hello'.center(20)

'Hello'.center(20, '=')

# picnicTable.py


def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))
picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)

works ! !

"""
# 134 - 135
# cmd python
# ctrl + z to exit
"""

# Removing Whitespace with strip(), rstrip(), and lstrip()

spam = ' Hello World '

spam.strip()

spam.lstrip()

spam.rstrip()


spam = 'SpamSpamBaconSpamEggsSpamSpam'

spam.strip('ampS')


# Copying and Pasting Strings with the pyperclip Module

# import pyperclip

# pyperclip.copy('Hello world!')

# pyperclip.paste()

# pyperclip.paste()

sort of works!!

"""
# 137
# cmd python
# ctrl + z to exit
"""

#! python3
# pw.py - An insecure password locker program.

import sys
PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}

# Step 2: Handle Command Line Arguments

#! python3
# pw.py - An insecure password locker program.
PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]  # first command line arg is the account name

works!!

"""
# 137 - 138
# cmd python
# ctrl + z to exit
"""

# Step 3: Copy the Right Password

#! python3
# pw.py - An insecure password locker program.

PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}

# import sys, pyperclip
if len(sys.argv) < 2:
    print('Usage: py pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]  # first command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)

sort of works!!

"""