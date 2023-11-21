import random

from data import data

in_progress = True
score = 0
vowels = "aeiouAEIOU"


def choose_random_persons(source, first_person=None):
    if not first_person:
        first_person = random.choice(source)
    source.remove(first_person)
    second_person = random.choice(source)
    return first_person, second_person


def print_comparison(first_person, second_person):
    print(f"\nCompare A: {first_person['name']}, "
          f"{'an' if first_person['description'][0] in vowels else 'a'} {first_person['description']}, "
          f"from {first_person['country']}")
    print('\nVS\n')
    print(f"Compare B: {second_person['name']}, "
          f"{'an' if second_person['description'][0] in vowels else 'a'} {second_person['description']}, "
          f"from {second_person['country']}")


def compare(game_data):
    global in_progress
    global score
    person_A, person_B = choose_random_persons(game_data)
    print_comparison(person_A, person_B)
    answer = input("Who has more followers? Type 'A' or 'B': ")
    if (answer == 'A' and person_A['follower_count'] > person_B['follower_count'] or answer == 'B' and
            person_B['follower_count'] > person_A['follower_count']):
        score += 1
        compare(game_data)
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        in_progress = False


def start_game():
    game_data = data.copy()

    compare(game_data)


if __name__ == '__main__':
    start_game()
