# The Challenge:
# Write a program that picks a random integer from 1 to 100, and has players guess the number. The rules are:
# 1. If a player's guess is less than 1 or greater than 100, say "OUT OF BOUNDS"
# 2. On a player's first turn, if their guess is
# * within 10 of the number, return "WARM!"
# * further than 10 away from the number, return "COLD!"
# 3. On all subsequent turns, if a guess is
# * closer to the number than the previous guess return "WARMER!"
# * farther from the number than the previous guess, return "COLDER!"
# 4. When the player's guess equals the number, tell them they've guessed correctly *and* how many guesses it took!

import random

guess = random.randint(1, 100)
# print(guess)
nr = 1
myList = list()
value = 0
while nr < 10:
    nr = nr + 1
    value = input('Guess the number: ')
    myList.append(int(value))
    if (int(value) == guess):
        print('You guessed!!')
        break

    if len(myList) > 2:
        if abs(myList[-2] - guess) > abs(myList[-1] - guess):
            print('WARMER')
        else:
            print('COLDER')
        continue

    if int(value) < 1 or int(value) > 100:
        print('Out of bonds')
    elif abs(int(value) - guess) <= 10:
        print('WARM')
    else:
        print('COLD')
print(myList)
print('You guessed from ' + str(len(myList)) + ' tries!')