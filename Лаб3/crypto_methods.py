import string
import random

# a) Метод перестановки символов
def transposition_cipher(text, block_size):
    if not (4 <= block_size <= 8):
        raise ValueError("Размер блока должен быть от 4 до 8 символов.")
    
    padded_text = text + ' ' * ((block_size - len(text) % block_size) % block_size)
    blocks = [padded_text[i:i+block_size] for i in range(0, len(padded_text), block_size)]
    encrypted_text = ''.join([''.join(random.sample(block, len(block))) for block in blocks])
    return encrypted_text

# b) Метод гаммирования (сложение с гаммой)
def gamma_cipher(text, gamma):
    gamma = (gamma * (len(text) // len(gamma) + 1))[:len(text)]
    encrypted_text = ''.join(chr(ord(c) ^ ord(g)) for c, g in zip(text, gamma))
    return encrypted_text

# c) Шифр Виженера
def vigenere_cipher(text, keyword, encrypt=True):
    keyword = (keyword * (len(text) // len(keyword) + 1))[:len(text)]
    shift = 1 if encrypt else -1
    encrypted_text = ''.join(
        chr((ord(c) + shift * ord(k)) % 256) for c, k in zip(text, keyword)
    )
    return encrypted_text

# d) Шифр Полибия
def polybius_square_cipher(text):
    square = [['A', 'B', 'C', 'D', 'E'],
              ['F', 'G', 'H', 'I', 'K'],
              ['L', 'M', 'N', 'O', 'P'],
              ['Q', 'R', 'S', 'T', 'U'],
              ['V', 'W', 'X', 'Y', 'Z']]
    row_col_map = {square[r][c]: f"{r+1}{c+1}" for r in range(5) for c in range(5)}
    encrypted_text = ''.join(row_col_map.get(char.upper(), char) for char in text)
    return encrypted_text

# e) Шифр Плейфера
def playfair_cipher(text, keyword):
    keyword = ''.join(sorted(set(keyword), key=keyword.index))
    keyword = keyword.replace("J", "I")
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    matrix = keyword + ''.join(c for c in alphabet if c not in keyword)
    pairs = [(text[i], text[i + 1]) for i in range(0, len(text), 2)]
    encrypted_text = ""
    for a, b in pairs:
        if a == b:
            b = 'X'
        a_index = matrix.index(a)
        b_index = matrix.index(b)
        a_row, a_col = divmod(a_index, 5)
        b_row, b_col = divmod(b_index, 5)
        if a_row == b_row:
            encrypted_text += matrix[a_row * 5 + (a_col + 1) % 5] + matrix[b_row * 5 + (b_col + 1) % 5]
        elif a_col == b_col:
            encrypted_text += matrix[((a_row + 1) % 5) * 5 + a_col] + matrix[((b_row + 1) % 5) * 5 + b_col]
        else:
            encrypted_text += matrix[a_row * 5 + b_col] + matrix[b_row * 5 + a_col]
    return encrypted_text

# f) Аффинный шифр
def affine_cipher(text, a, b, encrypt=True):
    if not (0 < a < 26 and 0 <= b < 26):
        raise ValueError("a должно быть от 1 до 25, b - от 0 до 25.")
    
    a_inv = pow(a, -1, 26) if encrypt else a
    result = ''
    for char in text.upper():
        if char in string.ascii_uppercase:
            num = ord(char) - ord('A')
            if encrypt:
                result += chr(((a * num + b) % 26) + ord('A'))
            else:
                result += chr(((a_inv * (num - b)) % 26) + ord('A'))
        else:
            result += char
    return result
