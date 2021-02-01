print("Добрый вечер")
all_seconds = int(input("Введите интересующее вас время в секундах: "))
minutes = all_seconds // 60
seconds = all_seconds % 60
hours = minutes // 60
minutes = minutes % 60
print(f"Введённое вами количество секунд можно преобразовать в {hours}:{minutes}:{seconds} часов")