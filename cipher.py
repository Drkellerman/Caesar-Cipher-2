# Caesar-cipher shift alphanumerical output five positions to the right:
SECRET_Key= 5
ALPHABET= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def caesar_encrypt(message, key):
    encrypted_result = ""

    # Loop back over to the original statement

for initial_character in message:

    # Alphabetic Item
    alphabetic_index= ALPHABET.find(initial_character)
    if alphabetic_index >=0:

        new_index= alphabetic_index

        new_index= alphabetic_index + SECRET_Key
        new_index = new_index % len(ALPHABET)

        new_character= ALPHABET[new_index]

        encrypted_result += new_character

    else:
        encrypted_result += initial_character

print encrypted_result

original_message= input("Engter your message that you want to encrypt: ")
original_message= original_message.upper()
