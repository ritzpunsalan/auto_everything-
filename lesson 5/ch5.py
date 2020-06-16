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