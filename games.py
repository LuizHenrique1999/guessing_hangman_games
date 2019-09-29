import hangman
import guessing


def choose_game():

    print('*****************************')
    print('********Choose game!*********')
    print('*****************************')

    print('(1) Hangman (2) Guessing')

    game = int(input('What game do you want to play?: '))

    if game == 1:
        hangman.play()
    elif game == 2:
        guessing.play()


if __name__ == '__main__':
    choose_game()
