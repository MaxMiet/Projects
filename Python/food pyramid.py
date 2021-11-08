from random import randint
from random import choice
import random
import os
import json
import sys

print('Enter your desired mode: Add or Food. \n"Add" allows you to add new foods to the list and "Food" chooses a random food from the list.')
print()

command = input('>')
cmd1 = 'Food'
cmd2 = 'Add'

#food command to randomly choose something from the list
if command.casefold() == cmd1.casefold():
    while True:
        FL = open('C:/Code/foodlist.txt').read().splitlines()
        result_line = random.choice(FL)
        print('Food choice: ' + result_line)
        cycle = input('>')
        if cycle.casefold() != cmd1.casefold():
            input('Incorrect input. Shutting down.')
            break

#add command to add user input to a new line on the list
elif command.casefold() == cmd2.casefold():
    while True:
        FL = open('C:/Code/foodlist.txt', 'a')
        printout = print('Enter the food name you\'d like to add.')
        user_input = input('>')
        new_line = ('\n' + (user_input))
        FL.write(new_line)
        print(user_input + ' added to the list.')
        cycle = input('>')
        if cycle.casefold() != cmd2.casefold():
            input('Incorrect input. Shutting down.')
            break
else:
    input('Incorrect input. Shutting down.')