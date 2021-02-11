def int_func(words):
    for el in words:
        if ord(el) == 32:
            pass
        elif ord(el) > 122:
            return "Неверные символы"
        elif ord(el) < 97:
            return "Неверные символы"
    return words.title()


print(int_func(input("Введите слово из строчных латинских букв: ")))
