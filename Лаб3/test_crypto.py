from crypto_methods import (
    transposition_cipher, gamma_cipher, vigenere_cipher,
    polybius_square_cipher, playfair_cipher, affine_cipher
)

# Тестируем метод перестановки символов
text = "HELLOWORLD"
print(f"Изначальный текст: {text}")
print("Метод перестановки символов:", transposition_cipher(text, 5))

# Тестируем метод гаммирования
gamma = "GAMMA"
print("Гаммирование:", gamma_cipher(text, gamma))

# Тестируем шифр Виженера
keyword = "KEY"
print("Шифр Виженера:", vigenere_cipher(text, keyword))
print("Расшифровка Виженера:", vigenere_cipher(vigenere_cipher(text, keyword), keyword, encrypt=False))

# Тестируем шифр Полибия
print("Шифр Полибия:", polybius_square_cipher(text))

# Тестируем шифр Плейфера
keyword = "KEYWORD"
print("Шифр Плейфера:", playfair_cipher(text, keyword))

# Тестируем аффинный шифр
a, b = 5, 8
print("Аффинный шифр:", affine_cipher(text, a, b))
print("Аффинная расшифровка:", affine_cipher(affine_cipher(text, a, b), a, b, encrypt=False))
