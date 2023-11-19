import random

from art import logo

cards = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
         '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10,
         'Q': 10, 'K': 10, 'A': 11}


def ask_to_play():
    want_to_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if want_to_play == 'y':
        start_game()


def compare(user_score, computer_score):
    # Bug fix. If you and the computer are both over, you lose.
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"

    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def give_cards(hand: list, count: int):
    for _ in range(count):
        given_card = random.choice(list(cards.keys()))
        hand.append(given_card)
    return sum([cards[card] for card in hand])


def start_game():
    my_cards = []
    computers_cards = []

    print('\n' * 10)
    print(logo)

    my_score = give_cards(my_cards, 2)
    computers_score = give_cards(computers_cards, 2)

    print(f'\tYour cards: {my_cards}, current score: {my_score}')
    print(f'\tComputer\'s first card: {computers_cards[0]}')

    if my_score == 21 or computers_score == 21:
        print(f'\tYour final hand: {my_cards}, final score: {my_score}')
        print(f'\tComputer\'s final hand: {computers_cards}, final score: {computers_score}')
        print(compare(my_score, computers_score))
        ask_to_play()

    answer = input("Type 'y' to get another card, type 'n' to pass: ")
    if answer == 'y':
        my_score = give_cards(my_cards, 1)

    while computers_score < 17:
        computers_score = give_cards(computers_cards, 1)

    print(f'\tYour final hand: {my_cards}, final score: {my_score}')
    print(f'\tComputer\'s final hand: {computers_cards}, final score: {computers_score}')
    print(compare(my_score, computers_score))
    
    ask_to_play()


if __name__ == '__main__':
    ask_to_play()
