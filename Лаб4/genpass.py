def next_letter(c):
    """Возвращает следующую букву в алфавите, если 'z', возвращает 'a'"""
    if c == 'z':
        return 'a'
    elif c == 'Z':
        return 'A'
    return chr(ord(c) + 1)

def prev_letter(c):
    """Возвращает предыдущую букву в алфавите, если 'a', возвращает 'z'"""
    if c == 'a':
        return 'z'
    elif c == 'A':
        return 'Z'
    return chr(ord(c) - 1)

def generate_password(word1, word2, word3):
    # 1. Первый символ: следующее за первым символом третьего слова
    first_char = next_letter(word3[0])

    # 2. Второй символ: предыдущая буква перед первым символом второго слова
    second_char = prev_letter(word2[0])

    # 3. Третий символ: в зависимости от длины третьего слова
    if len(word3) % 2 == 1:  # Нечетное количество символов
        middle_char = word3[len(word3) // 2]  # Средний символ
        third_char = next_letter(middle_char)
    else:  # Четное количество символов
        middle_left_char = word3[len(word3) // 2 - 1]  # Первый из двух средних символов
        third_char = prev_letter(middle_left_char)

    # 4. Четвертый символ: буква, соответствующая позиции суммы длин слов минус 2
    sum_length = len(word1) + len(word2) - 2
    fourth_char = chr(ord('a') + sum_length % 26)

    # Формируем и возвращаем результат
    return first_char + second_char + third_char + fourth_char

# Исходные данные
word1 = "Kats"
word2 = "milk"
word3 = "smitten"

# Генерация пароля
password = generate_password(word1, word2, word3)

# Вывод результата
print(f"Полученный пароль: {password}")
