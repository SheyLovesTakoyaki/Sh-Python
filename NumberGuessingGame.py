import random
random_number = random.randint(0, 10) # random number between 0 and 10
score = 0

while True:
    user_guess = (int(input('\nGuess a number: '))) # ask the user for their guess
    score += 1 # increase the score each guess

    # check if the guess is too low, high, or correct
    if user_guess > random_number:
        print('\nLower!') # hint: the guess is too high

    elif user_guess < random_number:
        print('\nHigher!') # hint: the guess is too low

    else:
        print('\n==== Correct! ====\n')
        print(f'Your score is {score}!')
        break # end the game