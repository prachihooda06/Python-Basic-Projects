import random


def guess_no(a):
    random_number = random.randint(1, a)
    guess_no = 0
    while guess_no != random_number:
        guess_no = int(input(f'Guess a number between 1 and {a}: '))
        if guess_no < random_number:
            print('Sorry, guess again too low.')
        elif guess_no > random_number:
            print('Sorry, guess again too high.')
        else:
            print(f'Yayy! You guessed it correct.')

guess_no(10)
