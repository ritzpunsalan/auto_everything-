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

# 66
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
# 69

"""

def spam():
    print(eggs)
eggs = 42
spam()
print(eggs)

works!!

"""
# sameName.py

"""

def spam():
    eggs = 'spam local'
    print(eggs) # prints 'spam local'

def bacon():
    eggs = 'bacon local'
    print(eggs) # prints 'bacon local'
    spam()
    print(eggs) # prints 'bacon local'

eggs = 'global'
bacon()
print(eggs) # prints 'global'

works!!

"""

# sameName2.py
# 70

"""

def spam():
    global eggs
    eggs = 'spam'

eggs = 'global'
spam()
print(eggs)

works!!

"""

# sameName3.py
# 71

"""

def spam():
    global eggs
    eggs = 'spam'  # this is the global


def bacon():
    eggs = 'bacon'  # this is a local


def ham():
    print(eggs)  # this is the global


eggs = 42  # this is the global
spam()
print(eggs)

works!!

"""

# sameName4.py

"""

def spam():
    print(eggs)  # ERROR!
    eggs = 'spam local'


eggs = 'global'
spam()

error works!!

"""

# zeroDivide.py
# 72

"""

def spam(divideBy):
    return 42 / divideBy

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))

error works!!

"""

# 73

"""

def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument.')

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))

works!!

"""

"""

def spam(divideBy):
    return 42 / divideBy

try:
    print(spam(2))
    print(spam(12))
    print(spam(0))
    print(spam(1))
except ZeroDivisionError:
    print('Error: Invalid argument.')

works!!

"""

# guessTheNumber.py
# 74

"""

# This is a guess the number game.
secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')

#Ask the player to guess 6 times.
for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break  # this condition is the correct guess!

if guess == secretNumber:
    print('Good job! You guessed my number in ' +
          str(guessesTaken) + ' guesses!')
else:
    print('Nope.The number I was thinking of was ' + str(secretNumber))

works!! 

"""
