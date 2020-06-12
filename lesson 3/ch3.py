""" 
chapter 3
    functions
pg 61
"""

# helloFunc.py
# 61
"""

def hello():
    print('Howdy!')
    print('Howdy!!!')
    print('Hello there.')

hello()
hello()
hello()

works!!

"""

# helloFunc2.py
# 63
"""

def hello(name):
    print('Hello ' + name)

hello('Alice')
hello('Bob')

works!!

"""

# magic8Ball.py
# 64
"""

import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'
 
r = random.randint(1, 9)
fortune = getAnswer(r)
print(fortune)

works!!

"""

# 65
"""

r = random.randint(1, 9)
fortune = getAnswer(r)
print(fortune)

print(getAnswer(random.randint(1, 9)))

does not work!!

"""

"""

spam = print('Hello!')

None == spam

semi works!!

"""

#66
"""

print('Hello')
print('World')

works!!

"""

"""

print('Hello', end='')
print('World')

works!!

"""

"""

print('cats', 'dogs', 'mice')

print('cats', 'dogs', 'mice', sep=',')

works!!

"""

# 68
"""

def spam():
    eggs = 31337

spam()
print(eggs)

works as an error should!!

"""

"""

def spam():
    eggs = 99
    bacon()
    print(eggs)

def bacon():
    ham = 101
    eggs = 0

spam()

works!!

"""