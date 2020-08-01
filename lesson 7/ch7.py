""" 
chapter 7
    Lists
pg 147 - 172
"""
# 148
# cmd python
# ctrl + z to exit

# Finding Patterns of Text Without Regular Expressions
# isPhoneNumber.py

"""

def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True


print('415-555-4242 is a phone number:')
print(isPhoneNumber('415-555-4242'))
print('Moshi moshi is a phone number:')
print(isPhoneNumber('Moshi moshi'))

works!!

"""
# 150 - 151
# cmd python
# ctrl + z to exit
"""

# Finding Patterns of Text With Regular Expressions
# Creating Regex Objects


import re
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

# Passing Raw Strings to re.compile()
# Matching Regex Objects

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

mo = phoneNumRegex.search('My number is 415-555-4242.')

print('Phone number found: ' + mo.group())

works!!

"""
# 152
# cmd python
# ctrl + z to exit
"""

# Review of Regular Expression Matching

# More Pattern Matching with Regular Expressions

# Grouping with Parentheses

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')

mo = phoneNumRegex.search('My number is 415-555-4242.')

mo.group(1)

mo.group(2)

mo.group(0)

mo.group()

works!!

"""
# 153
# cmd python
# ctrl + z to exit
"""

mo.groups()

areaCode, mainNumber = mo.groups()

print(areaCode)

print(mainNumber)


phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')

mo = phoneNumRegex.search('My phone number is (415) 555-4242.')

mo.group(1)

mo.group(2)

# Matching Multiple Groups with the Pipe

heroRegex = re.compile(r'Batman|Tina Fey')

mo1 = heroRegex.search('Batman and Tina Fey.')

mo1.group()


mo2 = heroRegex.search('Tina Fey and Batman.')

mo2.group()

works!!

"""
# 154 - 155
# cmd python
# ctrl + z to exit
"""

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')

mo = batRegex.search('Batmobile lost a wheel')

mo.group()

mo.group(1)

# Optional Matching with the Question Mark

batRegex = re.compile(r'Bat(wo)?man')

mo1 = batRegex.search('The Adventures of Batman')

mo1.group()


mo2 = batRegex.search('The Adventures of Batwoman')

mo2.group()

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')

mo1 = phoneRegex.search('My number is 415-555-4242')

mo1.group()

mo2 = phoneRegex.search('My number is 555-4242')

mo2.group()

works!!

"""
# 155 - 156
# cmd python
# ctrl + z to exit

# Matching Zero or More with the Star
"""

batRegex = re.compile(r'Bat(wo)*man')

mo1 = batRegex.search('The Adventures of Batman')

mo1.group()


mo2 = batRegex.search('The Adventures of Batwoman')

mo2.group()


mo3 = batRegex.search('The Adventures of Batwowowowoman')

mo3.group()

# Matching One or More with the Plus

batRegex = re.compile(r'Bat(wo)+man')

mo1 = batRegex.search('The Adventures of Batwoman')

mo1.group()


mo2 = batRegex.search('The Adventures of Batwowowowoman')

mo2.group()

mo3 = batRegex.search('The Adventures of Batman')

mo3 == None

works!!

"""
# 156
# cmd python
# ctrl + z to exit

# Matching Specific Repetitions with Curly Brackets
"""

haRegex = re.compile(r'(Ha){3}')

mo1 = haRegex.search('HaHaHa')

mo1.group()


mo2 = haRegex.search('Ha')

mo2 == None

works!!

"""
# 156 - 157
# cmd python
# ctrl + z to exit
"""

# Greedy and Nongreedy Matching

greedyHaRegex = re.compile(r'(Ha){3,5}')

mo1 = greedyHaRegex.search('HaHaHaHaHa')

mo1.group()


nongreedyHaRegex = re.compile(r'(Ha){3,5}?')

mo2 = nongreedyHaRegex.search('HaHaHaHaHa')

mo2.group()

# The findall() Method

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

mo = phoneNumRegex.search('Cell: 415-555-9999 Work: 212-555-0000')

mo.group()

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')  # has no groups

phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')

works!!

"""
# 158
# cmd python
# ctrl + z to exit
"""

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')  # has groups

phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')

# Character Classes

xmasRegex = re.compile(r'\d+\s\w+')

xmasRegex.findall(
    '12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')

works!!

"""
# 159
# cmd python
# ctrl + z to exit
"""

# Making Your Own Character Classes

vowelRegex = re.compile(r'[aeiouAEIOU]')

vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')


consonantRegex = re.compile(r'[^aeiouAEIOU]')

consonantRegex.findall('RoboCop eats baby food. BABY FOOD.')


works!!

"""
# 159 - 160
# cmd python
# ctrl + z to exit
"""

# The Caret and Dollar Sign Characters

beginsWithHello = re.compile(r'^Hello')

beginsWithHello.search('Hello world!')

beginsWithHello.search('He said hello.') == None

endsWithNumber = re.compile(r'\d$')

endsWithNumber.search('Your number is 42')

endsWithNumber.search('Your number is forty two.') == None

wholeStringIsNum = re.compile(r'^\d+$')

wholeStringIsNum.search('1234567890')

wholeStringIsNum.search('12345xyz67890') == None

wholeStringIsNum.search('12 34567890') == None


# The Wildcard Character

atRegex = re.compile(r'.at')

atRegex.findall('The cat in the hat sat on the flat mat.')


works!!

"""
# 161
# cmd python
# ctrl + z to exit
"""

# Matching Everything with Dot-Star
# import re

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
mo.group(1)

mo.group(2)


nongreedyRegex = re.compile(r'<.*?>')
mo = nongreedyRegex.search('<To serve man> for dinner.>')
mo.group()


greedyRegex = re.compile(r'<.*>')
mo = greedyRegex.search('<To serve man> for dinner.>')
mo.group()

works!!

"""
# 162
# cmd python
# ctrl + z to exit
"""

# Matching Newlines with the Dot Character

noNewlineRegex = re.compile('.*')
noNewlineRegex.search('Serve the public trust.\nProtect the innocent. \nUphold the law.').group()

newlineRegex = re.compile('.*', re.DOTALL)
newlineRegex.search('Serve the public trust.\nProtect the innocent. \nUphold the law.').group()

works!!

"""
# 163
# cmd python
# ctrl + z to exit
"""

# Case-Insensitive Matching

regex1 = re.compile('RoboCop')
regex2 = re.compile('ROBOCOP')
regex3 = re.compile('robOcop')
regex4 = re.compile('RobocOp')

robocop = re.compile(r'robocop', re.I)
robocop.search('RoboCop is part man, part machine, all cop.').group()


robocop.search('ROBOCOP protects the innocent.').group()


robocop.search('Al, why does your programming book talk about robocop so much?').group()


# Substituting Strings with the sub() Method

namesRegex = re.compile(r'Agent \w+')
namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')

works!!

"""
# 164
# cmd python
# ctrl + z to exit
"""

import re

agentNamesRegex = re.compile(r'Agent (\w)\w*')
agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')


# Managing Complex Regexes

# Combining re.IGNORECASE, re.DOTALL, and re.VERBOSE

works!!

"""
# 165
# cmd python
# ctrl + z to exit
"""

import re

someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL)

someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)

works sort of!!

"""