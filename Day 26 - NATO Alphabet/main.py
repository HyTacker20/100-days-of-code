import pandas

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_dict = {row.letter: row.code for index, row in data.iterrows()}
print(data_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Write word: ")
result = [data_dict[letter.upper()] for letter in word]
print(result)
