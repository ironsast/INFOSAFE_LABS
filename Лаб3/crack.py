from functions import decryption, reading
from additional_functions import program_info, text_statistics, license_check

voc = [' и ', ' в ', ' не ', ' на ', ' что ', ' по ', ' к ', ' но ', ' у ', ' как ']

def finding(word, ciphertext):
    for i in range(len(ciphertext) - len(word)):
        g = [ord(ciphertext[i + j]) - ord(word[j]) for j in range(len(word))]
        s = 0
        for k in range(len(g)):
            if g[k] == g[0]:
                s += 1
        if s == len(g):
            return g[0]
    return None

def main():
    if not license_check():
        print("[-] Программа завершена из-за отсутствия лицензии.")
        return
    
    program_info()
    CipherText = reading()
    print("Пытаюсь найти ключ методом частотного анализа...")

    for word in voc:
        key = finding(word, CipherText)
        if key is not None:
            PlainText = decryption(key, CipherText)
            print(f"\n[+] Ключ подобран: {key}")
            print("Расшифрованный текст:")
            print(PlainText)
            print("\nСтатистика зашифрованного текста:")
            text_statistics(CipherText)
            print("Статистика расшифрованного текста:")
            text_statistics(PlainText)
            break
    else:
        print("[-] Ключ не найден.")

if __name__ == "__main__":
    main()
