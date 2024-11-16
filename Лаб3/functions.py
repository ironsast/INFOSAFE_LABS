def encryption(Key, PlainText):
    CipherText = ''
    for p in PlainText:
        code = ord(p) + Key
        CipherText += chr(code)
    return CipherText

def decryption(Key, CipherText):
    PlainText = ''
    for p in CipherText:
        code = ord(p) - Key
        PlainText += chr(code)
    return PlainText

def reading():
    source = input("Источник данных: \n 'к' - консоль \t 'ф' - файл \n")
    if source == 'к':
        data = input('Введите текст: ').strip()
        return data
    elif source == 'ф':
        filename = input("Название файла с данными в формате '*.txt': \n")
        with open(filename, 'r', encoding='cp1251') as f:
            data = f.read()
        return data
    else:
        print("[-] Выбрана неверная операция")

def writing(data, operation):
    op = operationtype(operation)
    exit = input("Вид вывода данных: \n 'к' - консоль \t 'ф' - файл: \n")
    if exit == 'к':
        print("Результат: ", data)
    elif exit == 'ф':
        filename = input(f"Файл для вывода результата {op} в формате 'имя.txt': \n")
        with open(filename, 'w', encoding='cp1251') as f:
            f.write(data)
        print(f"\n[+] Результат {op} записан в файл {filename}")
    else:
        print("[-] Выбрана неверная операция")

def operationtype(operation):
    return "шифрования" if operation == "ш" else "расшифрования"
