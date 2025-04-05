import random

random_number = random.randint(0, 10)
score = 0

while True:
    # ask the user
    user_guess = (int(input('\nGuess a number: ')))
    score += 1

    # keep guessing
    if user_guess > random_number:
        print('\nLower!')

    elif user_guess < random_number:
        print('\nHigher!')

    else:
        print('\n==== Correct! ====\n')
        print(f'Your score is {score}!')
        break