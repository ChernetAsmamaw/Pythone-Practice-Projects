# There will be a secert number and an input option to guess it
# If the guess is incorrect the input question will be repeated till the guess is similar to the secret number

secret_number = 9

while True:
    guess = eval(input('Guess the secret number between 1 and 10: '))

    if guess == secret_number:
        print('You guessed it right!')
        break