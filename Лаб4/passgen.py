import random
import string
import time

# Определение групп символов
digits = string.digits  # Цифры (0-9)
lowercase_russian = 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя'  # Русские строчные буквы

# Объединение всех символов в один алфавит
alphabet = digits + lowercase_russian

# Длина пароля
L = 5

# Генерация случайного пароля
def generate_password(length):
    return ''.join(random.choice(alphabet) for _ in range(length))

# Расчет времени взлома
def calculate_crack_time(password_length, alphabet_size, attempts_per_second):
    # Вычисление времени взлома по формуле
    total_combinations = alphabet_size ** password_length
    time_to_crack_seconds = total_combinations / attempts_per_second
    
    # Перевод времени в дни
    time_to_crack_days = time_to_crack_seconds / (60 * 60 * 24)
    
    return time_to_crack_days

# Генерация пароля
password = generate_password(L)
print(f"Сгенерированный пароль: {password}")

# Мощность алфавита
alphabet_size = len(alphabet)

# Скорость перебора паролей (пароли/сек)
attempts_per_second = 20

# Время взлома пароля в днях
crack_time = calculate_crack_time(L, alphabet_size, attempts_per_second)
print(f"Ожидаемое время взлома пароля: {crack_time:.2f} дней")

