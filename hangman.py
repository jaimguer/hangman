
import random

possible_words = ['apple', 'banana', 'orange', 'grape', 'strawberry', 'raspberry', 'blackberry']

board = []
word = None

NUMBER_OF_GUESSES = 10

BLANK_MARKER = '_'

def reveal_letter(guess):
    if guess in list(word):
        print("Got one!")
        indices = [index for index, char in enumerate(word) if char == guess]
        for index in indices:
            board[index] = guess
    else:
        print("Sorry, {0} is not in the word!".format(guess))
    print(board)


def generate_initial_board():
    """ Select a random word and generate the user-faceing blank board"""
    print("Welcome to hangman! Let's get started. This is your starting board:")
    global board
    global word
    word = random.choice(possible_words)
    board = [BLANK_MARKER] * len(word)
    print(board)
    print("You have {0} guesses remaining".format(NUMBER_OF_GUESSES))


def is_done():
    """ Determine if the game is over """
    global NUMBER_OF_GUESSES
    out_of_turns = NUMBER_OF_GUESSES < 0
    got_the_word = BLANK_MARKER not in board
    if got_the_word:
        print("Congratulations! You got the word!")

    if out_of_turns:
        print("You're out of guesses!")

    return out_of_turns or got_the_word


def main():
    generate_initial_board()
    while not is_done() :
        guess = input("Take a guess: ")
        reveal_letter(guess)
        global NUMBER_OF_GUESSES
        NUMBER_OF_GUESSES -= 1
        print("Number of guesses left: {0}".format(NUMBER_OF_GUESSES))
    print("Game over!")


if __name__ == "__main__":
    main()
