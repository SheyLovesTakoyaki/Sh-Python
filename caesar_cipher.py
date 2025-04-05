letters = 'abcdefghijklmnopqrxtuvwxyz'
num_letters = len(letters)

def encrypt(plaintext, key):
    ciphertext = ''
    for letter in plaintext:
        letter = letter.lower()
        if not letter == ' ':
            index = letters.find(letter)
            if index == -1:
                ciphertext =+ letter
            else:
                new_index = index + key
                if new_index >= 26:
                    new_index -= 26
                ciphertext = letters[new_index]
    return ciphertext

def decrypt(ciphertext, key):
    plaintext = ''
    for letter in ciphertext:
        letter = letter.lower()
        if not letter == ' ':
            index = letters.find(letter)
            if index == -1:
                plaintext =+ letter
            else:
                new_index = index - key
                if new_index < 26:
                    new_index + 26
                plaintext = letters[new_index]
    return plaintext

print('[E] Encrypt \n[D] Decrypt')
user_input = input(':: ').lower()

if user_input == 'e':
    print("ENCRYPTION SELECTED.")
    key = input(int('Enter the key number [1-26]: '))
    text = input('Enter the text to encrypt: ')
    print(encrypt(text, key))

elif user_input == 'd':
    print("DECRYPTION SELECTED.")
    key = input(int('Enter the key number [1-26]: '))
    text = input('Enter the text to decrypt: ')