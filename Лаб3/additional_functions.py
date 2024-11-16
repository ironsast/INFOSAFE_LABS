from functions import encryption, decryption, reading, writing
from collections import Counter
import datetime

def program_info():
    print("Метод шифрования: Caesar Cipher")
    print("Автор: Иван Иванов")
    print("Дата разработки: 14 ноября 2024 года")

def text_statistics(text):
    stats = Counter(text)
    total_chars = len(text)
    print("Статистика символов в тексте:")
    for char, freq in stats.items():
        print(f"Символ: '{char}' — Частота: {freq} ({(freq / total_chars) * 100:.2f}%)")
    print(f"Всего символов: {total_chars}")

def license_check():
    valid_key = "12345-ABCDE"
    license_duration_days = 30
    user_key = input("Введите лицензионный ключ: ")
    if user_key != valid_key:
        print("[-] Неверный ключ! Доступ запрещен.")
        return False
    try:
        with open("license_date.txt", "r") as f:
            activation_date = datetime.datetime.strptime(f.read().strip(), "%Y-%m-%d")
    except FileNotFoundError:
        activation_date = datetime.datetime.now()
        with open("license_date.txt", "w") as f:
            f.write(activation_date.strftime("%Y-%m-%d"))
    current_date = datetime.datetime.now()
    if (current_date - activation_date).days > license_duration_days:
        print("[-] Срок действия лицензии истек.")
        return False
    print("[+] Лицензия действительна.")
    return True

# Основной блок
if license_check():
    program_info()
    Key = int(input("Введите ключ шифрования: "))
    operation = input("Введите 'ш' для шифрования, 'р' для расшифрования: ")
    if operation == 'ш':
        PlainText = reading()
        CipherText = encryption(Key, PlainText)
        print("\n[+] Шифрование завершено\n")
        writing(CipherText, operation)
        print("Статистика исходного текста:")
        text_statistics(PlainText)
        print("Статистика зашифрованного текста:")
        text_statistics(CipherText)
    elif operation == 'р':
        CipherText = reading()
        PlainText = decryption(Key, CipherText)
        print("\n[+] Расшифрование завершено\n")
        writing(PlainText, operation)
        print("Статистика зашифрованного текста:")
        text_statistics(CipherText)
        print("Статистика расшифрованного текста:")
        text_statistics(PlainText)
    else:
        print("[-] Выбрана неверная операция")
else:
    print("[-] Программа завершена из-за отсутствия лицензии.")
