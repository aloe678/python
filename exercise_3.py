print("Hello, human")
print("Вычислим число по формуле n + nn + nnn")
while True:
    number = int(input("Введите положительное однозначное число: "))
    if number < 10 and number > 0:
        summ_number = number + number * 11 + number * 111
        print("Получилось ", summ_number)
        break
    else:
        print("Это число не подходит")
        continue