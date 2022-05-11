"""
DIRECTIONS:
A lucky number is a number who is composed exclusively of 4's and 7's.
A nearly lucky number is a number which the sum of all lucky digits equals a lucky number.

For a given input value, print YES if a number is nearly lucky and NO otherwise.
"""


# Counts the amount of 4's and 7's.
def countLuckyCharacters(num):
    luckyTotal = 0
    for i in range(0, len(num)):
        curr = num[i]
        if curr == '4' or curr == '7':
            luckyTotal += 1
    return luckyTotal


userInput = input()

# Count the lucky characters of the input.
luckyCount = str(countLuckyCharacters(userInput))
# If there are as many lucky characters as the length of the number, all characters are lucky.
print('YES' if countLuckyCharacters(luckyCount) == len(luckyCount) else 'NO')
