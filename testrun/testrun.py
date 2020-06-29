"""
    source link:
E:\Desktop\neccessy books for coding\python books\automate python
E:\Desktop\neccessy books for coding\python books
E:\Desktop\neccessy books for coding\python books\automate python\testrun

"""
# chapter: 4
# This program says hello and asks for my name.

# allMyCats1.py
# 100

# Passing References

def eggs(someParameter):
    someParameter.append('Hello')

spam = [1, 2, 3]
eggs(spam)
print(spam)

import copy
spam = ['A', 'B', 'C', 'D']
cheese = copy.copy(spam)
cheese[1] = 42
print(spam)
print(cheese)