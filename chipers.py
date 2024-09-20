import numpy as np

def vigenere_encrypt(plain_text, key):
    key = key.upper()
    plain_text = plain_text.upper()
    result = []

    for i in range(len(plain_text)):
        char = plain_text[i]
        if char.isalpha():
            shift = ord(key[i % len(key)]) - ord('A')
            encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            result.append(encrypted_char)
        else:
            result.append(char)
    return ''.join(result)

def vigenere_decrypt(cipher_text, key):
    key = key.upper()
    cipher_text = cipher_text.upper()
    result = []

    for i in range(len(cipher_text)):
        char = cipher_text[i]
        if char.isalpha():
            shift = ord(key[i % len(key)]) - ord('A')
            decrypted_char = chr((ord(char) - ord('A') - shift + 26) % 26 + ord('A'))
            result.append(decrypted_char)
        else:
            result.append(char)
    return ''.join(result)

def create_playfair_matrix(key):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    matrix = []
    used_chars = set()

    key = key.upper().replace("J", "I")

    for char in key:
        if char not in used_chars and char in alphabet:
            matrix.append(char)
            used_chars.add(char)

    for char in alphabet:
        if char not in used_chars:
            matrix.append(char)

    return [matrix[i:i + 5] for i in range(0, 25, 5)]

def playfair_encrypt(plain_text, key):
    # Placeholder untuk Playfair encryption
    return "Playfair Encrypted Text"

def playfair_decrypt(cipher_text, key):
    # Placeholder untuk Playfair decryption
    return "Playfair Decrypted Text"

def hill_encrypt(plain_text, key_matrix):
    # Placeholder untuk Hill encryption
    return "Hill Encrypted Text"

def hill_decrypt(cipher_text, key_matrix):
    # Placeholder untuk Hill decryption
    return "Hill Decrypted Text"
