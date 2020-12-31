alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabet_rev=[]
for letter in reversed(alphabet):
    alphabet_rev += letter


def encode(word, num):
    encoded = ""
    for letter in word:
        position = alphabet.index(letter)
        new_pos = position + num
        encoded += alphabet[new_pos]
    print(f"The encoded text is : {encoded}")


def decode(word, num):
    decoded = ""
    for letter in word:
        position = alphabet.index(letter)
        new_pos = position - num
        decoded += alphabet[new_pos]
    print(f"The encoded text is : {decoded}")


command = input('Enter encode to encrypt, or decode to decrypt: ')
if command.lower() == 'encode':
    word = input('Enter the message without spaces to encrytp: ')
    num = int(input('Enter the number of shifts'))
    encode(word, num)
elif command.lower() == 'decode':
    word = input("Enter the message without spaces to encrypt")
    num = int(input("Enter the number of shifts: "))
    decode(word, num)
else:
    print('Wrong input')
