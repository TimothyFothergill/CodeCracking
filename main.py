decryption_dictionary = {
    "a": "!", "b": ")", "c": "\"", "d": "(", "e": "£",
    "f": "*", "g": "%", "h": "&", "i": ">", "j": "<",
    "k": "@", "l": "a", "m": "b", "n": "c", "o": "d",
    "p": "e", "q": "f", "r": "g", "s": "h", "t": "i",
    "u": "j", "v": "k", "w": "l", "x": "m", "y": "n",
    "z": "o"
    }

dictionary_keys = list(decryption_dictionary.keys())
dictionary_values = list(decryption_dictionary.values())


def user_selection():
    string = input("Do you wish to encrypt or decrypt a message? [e]ncrypt/[d]ecrypt: ")
    if string.upper() == "E" or string.upper() == "ENCRYPT":
        user_encrypt_message()
    elif string.upper() == "D" or string.upper() == "DECRYPT":
        user_decrypt_message()
    else:
        return string


def user_encrypt_message():
    print("Available characters to encrypt: " + str(dictionary_keys))
    string = input("Enter a message to encrypt: ").lower()
    message_to_encrypt = list(string)
    encrypted_message = []
    for letter in message_to_encrypt:
        encrypted_letter = decryption_dictionary.get(letter)
        encrypted_message.append(encrypted_letter)
    encrypted_string = ""
    for letter in encrypted_message:
        encrypted_string += letter
    print("Your encrypted message: " + encrypted_string)


def user_decrypt_message():
    print("Available characters to decrypt: " + str(dictionary_values))
    string = input("Enter a message to decrypt: ").lower()
    message_to_decrypt = list(string)
    decrypted_message = []
    for letter in message_to_decrypt:
        decrypted_letter = dictionary_keys[dictionary_values.index(letter)]
        decrypted_message.append(decrypted_letter)
    decrypted_string = ""
    for letter in decrypted_message:
        decrypted_string += letter
    print("Your encrypted message: " + decrypted_string)

# a b c d e f g h i j k l m n o p q r s t u v w x y z
# ! ) " ( £ * % & > < @ a b c d e f g h i j k l m n o

user_selection()
