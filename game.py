# Write your code here
import random

winners = {'rock': 'paper', 'paper': 'scissors', 'scissors': 'rock'}
choices = ['rock', 'fire', 'scissors', 'snake', 'human', 'tree', 'wolf', 'sponge', 'paper', 'air', 'water', 'dragon',
           'devil', 'lightning', 'gun']
choices2 = choices * 2
winners2 = {}
z = 1
for x in choices:
    winners2[x] = choices2[z:z + 7]
    z += 1

print('Enter your name:', end=' ')
username = input()
print(f'Hello, {username}')
my_file = open('rating.txt', 'r')
contents = [x.strip('\n') for x in my_file.readlines()]
my_file.close()
ratings = {}
for x in contents:
    z = x.split()
    ratings[z[0]] = int(z[1])
score = 0
if username in ratings.keys():
    score = ratings[username]
else:
    score = 0


def big_game(selection, score):
    user_input = ''
    while user_input != '!exit':
        user_input = input()
        if user_input == '!exit':
            print('Bye!')
        elif user_input == '!rating':
            print(f'Your rating: {score}')
        elif user_input not in selection:
            print('Invalid input')
        else:
            computer_choice = random.choice(selection)
            if user_input == computer_choice:
                print(f'There is a draw ({computer_choice})')
                score += 50
            elif user_input in winners2[computer_choice]:
                print(f'Sorry, but the computer chose {computer_choice}')
            else:
                print(f'Well done. The computer chose {computer_choice} and failed')
                score += 100


def small_game(winners, score):
    user_input = ''
    while user_input != '!exit':
        user_input = input()
        if user_input == '!exit':
            print('Bye!')
        elif user_input == '!rating':
            print(f'Your rating: {score}')
        elif user_input not in list(winners.keys()):
            print('Invalid input')
        else:
            computer_choice = random.choice(list(winners.keys()))
            if user_input == computer_choice:
                print(f'There is a draw ({computer_choice})')
                score += 50
            elif winners[user_input] == computer_choice:
                print(f'Sorry, but the computer chose {computer_choice}')
            else:
                print(f'Well done. The computer chose {computer_choice} and failed')
                score += 100


options = input()
if ',' not in options:
    print('Okay, let\'s start')
    small_game(winners, score)
else:
    selection = options.split(',')
    smallgame = False
    for x in selection:
        if x not in choices:
            smallgame = True

    if smallgame:
        print('Okay, let\'s start')
        small_game(winners, score)
        exit()
    else:
        print('Okay, let\'s start')
        big_game(selection, score)

