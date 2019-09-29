import random


def menu():

    print('*****************************')
    print('Welcome to the Guessing Game!')
    print('*****************************')

    print('What difficulty level do you want to play?')
    print('(1) Easy (2) Medium (3) Hard')


def level_choice(total_retries):

    level = int(input("Enter the level: "))

    if level == 1:
        total_retries = 20
    elif level == 2:
        total_retries = 10
    else:
        total_retries = 5
    return total_retries


def play():

    menu()
    total_retries = 0
    random_number = random.randrange(1, 101)
    points = 1000

    total_retries = level_choice(total_retries)

    for rounds in range(1, total_retries + 1):

        attempt = int(input("Enter a number between 1 and 100: "))
        print(f'You entered a number: {attempt}')
        print(f'Attempt {rounds} of {total_retries}')

        if attempt < 1 or attempt > 100:
            print('You must enter a number between 1 and 100!')
            continue

        got_right = attempt == random_number
        low_number = attempt < random_number
        high_number = attempt > random_number

        if got_right:
            print(f'Congratulations, you won!')
            break
        elif low_number:
            print('Sorry, you lost! Your number is below the secret number.')
        elif high_number:
            print('Sorry, you lost! Your number is above the secret number.')

        lost_points = abs(random_number - attempt)
        points = points - lost_points

    print(f'End of the game! You scored {points} points!')


if __name__ == '__main__':
    play()
