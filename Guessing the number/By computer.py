import random


def computer_guess(a):
    low = 1
    high = a
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f"Is {guess} too high(H), too low(L), or correct(C)?? ").lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f'Yay!! The computer guessed the correct number.')

computer_guess(80)
