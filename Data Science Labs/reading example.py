'''
target = open('hamlet.txt', 'r', encoding = 'utf8')
#text = target.readlines()

letterCount = {}
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for line in target:
    for letter in line:
        letter.lower()
        if letter in alphabet:
            if letter not in letterCount:
                letterCount[letter] = 1
            else:
                letterCount[letter] += 1
print(letterCount)
'''

