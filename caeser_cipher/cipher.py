from caeser_cipher.corpus_loader import name_list, word_list
import re

def encrypt(text, key):
    encrypted_text = ''

    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            encrypted_text += chr((ord(char) + key - 65) % 26 + 65)
        elif (char.islower()):
            encrypted_text += chr((ord(char) + key - 97) % 26 + 97)
        else:
            encrypted_text += char

    return encrypted_text


def decrypt(encrypted_text, key):
    return encrypt(encrypted_text, -key)


def count_words(text):
    # Credit to JB Tellez
    separated_words = text.split()
    word_count = 0

    for entry in separated_words:
        word = re.sub(r'[^A-Za-z]+','', entry)
        if word.lower() in word_list or word in name_list:
            word_count += 1

    return word_count


def crack(encrypted_text):

    for i in range(26):
        cracked_text = decrypt(encrypted_text, i)
        word_count = count_words(cracked_text)
        decimal = int(word_count / len(encrypted_text.split()))
        if decimal > .5:
            return cracked_text

    return ''
