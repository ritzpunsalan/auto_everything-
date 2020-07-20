"""
    source link:
E:\Desktop\neccessy books for coding\python books\automate python
E:\Desktop\neccessy books for coding\python books
E:\Desktop\neccessy books for coding\python books\automate python\testrun

"""
# chapter: 5
# This program says hello and asks for my name.

# birthdays.py
# 118
# ticTacToe.py

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
