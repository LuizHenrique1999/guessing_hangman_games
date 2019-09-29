import random


def play():

    presentation()

    secret_word = load_secret_word()

    hit_letters = initialize_hit_letters(secret_word)

    hanged = False
    got_right = False
    errors = 0

    print(hit_letters)

    while not hanged and not got_right:

        attempt = attempt_request()

        if attempt in secret_word:
            marca_chute_correto(attempt, hit_letters, secret_word)
        else:
            errors += 1
            draw_gallows(errors)
            print(f'Oops, you got it wrong! {6-errors} tries left.')
        if errors == 6:
            hanged = True
        print(hit_letters)
        got_right = '_' not in hit_letters

    if got_right:
        print_victorious_message()
    else:
        print_loser_message(secret_word)


def presentation():

    print('*****************************')
    print('Welcome to the hangman Game!!')
    print('*****************************')


def load_secret_word():

    archive = open("palavras.txt", "r")
    words = []

    for row in archive:
        row = row.strip()
        words.append(row)

    archive.close()

    number = random.randrange(0, len(words))
    secret_word = words[number].upper()
    return secret_word


def initialize_hit_letters(word):

    return ["_" for letter in word]


def attempt_request():

    attempt = input('What is the letter? ')
    attempt = attempt.strip().upper()
    return attempt


def marca_chute_correto(attempt, hit_letters, secret_word):

    index = 0
    for letter in secret_word:
        if attempt == letter:
            hit_letters[index] = letter
        index += 1


def print_victorious_message():

    print("Congratulations, you won!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def print_loser_message(secret_word):

    print("How sad, you were hanged!")
    print("The word was {}".format(secret_word))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def draw_gallows(errors):

    print("  _______     ")
    print(" |/      |    ")

    if errors == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if errors == 2:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if errors == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if errors == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if errors == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if errors == 6:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if errors == 7:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


if __name__ == '__main__':
    play()
