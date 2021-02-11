def int_func(word):
    for el in word:
        if ord(el) < 97:
            return "Неверные символы"
        elif ord(el) > 122:
            return "Неверные символы"
    return word.title()


print(int_func(input("Введите слово из строчных латинских букв: ")))
