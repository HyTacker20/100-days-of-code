alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
alphabet_length = len(alphabet)


def caesar_cipher(text, shift, direction):
    result = ""
    shift %= alphabet_length
    if direction == 'decode':
        shift *= -1

    for letter in text:
        if letter in alphabet:
            index = alphabet.index(letter)
            new_index = index + shift
            new_letter = alphabet[new_index]
            result += new_letter
        else:
            result += letter

    print(f"The {direction}d text is {result}")


if __name__ == '__main__':
    input_direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    input_text = input("Type your message:\n").lower()
    input_shift = int(input("Type the shift number:\n"))

    caesar_cipher(input_text, input_shift, input_direction)
