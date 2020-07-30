"""
    source link:
E:\Desktop\neccessy books for coding\python books\automate python
E:\Desktop\neccessy books for coding\python books
E:\Desktop\neccessy books for coding\python books\automate python\testrun

"""
# chapter: 7
# 159 - 160
# cmd python
# ctrl + z to exit

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
