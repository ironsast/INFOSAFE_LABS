from functions import encryption, decryption, reading, writing
from additional_functions import program_info, text_statistics, license_check

def main():
    if not license_check():
        print("[-] Программа завершена из-за отсутствия лицензии.")
        return
    
    program_info()
    Key = int(input("Введите ключ шифрования/дешифрования: "))
    operation = input("Введите 'ш' для шифрования или 'р' для дешифрования: ")
    
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
        print("\n[+] Дешифрование завершено\n")
        writing(PlainText, operation)
        print("Статистика зашифрованного текста:")
        text_statistics(CipherText)
        print("Статистика расшифрованного текста:")
        text_statistics(PlainText)
    
    else:
        print("[-] Выбрана неверная операция")

if __name__ == "__main__":
    main()
