"""
    source link:
E:\Desktop\neccessy books for coding\python books\automate python
E:\Desktop\neccessy books for coding\python books
E:\Desktop\neccessy books for coding\python books\automate python\testrun

"""
# chapter: 5
# This program says hello and asks for my name.

# birthdays.py
# 108
# The Dictionary Data Type

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