print('*****************************')
print('Welcome to the Guessing Game!')
print('*****************************')

secret_number = 42
total_retries = 3
round = 1

while total_retries >= round:

    attempt = int(input("Enter your secret number: "))
    print(f'You entered a number: {attempt}')
    print(f'Attempt {round} of {total_retries}')

    got_right = attempt == secret_number
    low_number = attempt < secret_number
    high_number = attempt > secret_number

    if got_right:
        print('Congratulations, you won!')
    elif low_number:
        print('Sorry, you lost! Your number is below the secret number.')
    elif high_number:
        print('Sorry, you lost! Your number is above the secret number.')
    round += 1
print('End of the game! Thank you!')



















