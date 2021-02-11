def my_func(name, surname, birth, town, email, phone):
    return f"{name} {surname}, {birth}, {town}, {email}, {phone}"


print(my_func(name=input("Имя: "), surname=input("Фамилия: "), birth=input("Дата рождения: "), town=input("Город: "), email=input("E-mail: "), phone=input("Телефон: ")))
