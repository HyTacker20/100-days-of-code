# Step 1
import random
from hangman_words import word_list

in_progress = True


def end_game():
    global in_progress
    in_progress = False


def print_word(word, guested_word):
    result = ''
    for letter, g_letter in zip(word, guested_word):
        if letter == g_letter:
            result += letter
        else:
            result += '_'


def start_game():
    HP = 5
    GUESSED_WORD = random.choice(word_list)
    GUESSED_WORD_COPY = GUESSED_WORD
    WORD = ['_' for _ in range(len(GUESSED_WORD))]
    print(''.join(WORD))
    while in_progress and HP != 0:
        letter = input("Please, write one letter: ")
        if letter in GUESSED_WORD_COPY:
            print("Nice! You guessed!")
            WORD[GUESSED_WORD_COPY.find(letter)] = letter
            GUESSED_WORD_COPY = GUESSED_WORD_COPY.replace(letter, '_', 1)
            print(''.join(WORD))
            if ''.join(WORD) == GUESSED_WORD:
                print(f"YOU WIN! {HP=}")
                end_game()
        else:
            HP -= 1
            if HP != 0:
                print('No! Try again!')
    else:
        print("YOU LOSE! HA-HA!") if HP == 0 else print()
        print(GUESSED_WORD)


if __name__ == '__main__':
    start_game()
